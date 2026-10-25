'use strict';
const $ = id => document.getElementById(id);
const storage = {get(key, fallback){try{return JSON.parse(localStorage.getItem(key)) ?? fallback;}catch{return fallback;}},set(key,value){try{localStorage.setItem(key,JSON.stringify(value));}catch{}}};
// Apply the smaller reading size once, including existing saved preferences.
if(!storage.get('d41-font-v2',false)){storage.set('d41-font',Math.max(15,(Number(storage.get('d41-font',18))||18)-2));storage.set('d41-font-v2',true);}
let chapters=[], pages=[], flip=null, font=storage.get('d41-font',16), rebuilding=false, flow=false;
let saved=storage.get('d41-place',null), resizeTimer;
font=Math.max(15,Math.min(24,Number(font)||16));
document.documentElement.style.setProperty('--font',`${font}px`);
document.body.classList.toggle('night',storage.get('d41-night',false));
const voicePattern=/^[A-ZÀ-Ü][A-ZÀ-ÜÇ ]{2,}$/;
function blocks(chapter){
  const result=[{tag:'h2',text:chapter.title,line:-1,className:''}]; let thought=false;
  chapter.lines.forEach((raw,line)=>{const text=raw.trim();if(!text)return;
    const voice=voicePattern.test(text)&&text.length<45;
    result.push({tag:'p',text,line,className:voice?'voice':thought?'thought':text.startsWith('—')?'dialogue':''});thought=voice;
  });return result;
}
function node(block,text=block.text){const el=document.createElement(block.tag);el.textContent=text;el.className=block.className;return el;}
function dimensions(){const narrow=innerWidth<850;const top=$('stage').getBoundingClientRect().top;const height=Math.max(280,innerHeight-top-64);const width=narrow?Math.max(230,Math.min(460,innerWidth-32)):Math.min(490,(innerWidth-90)/2);return {width:Math.floor(width),height:Math.floor(height)};}
function sheet(chapter,w,h){const el=document.createElement('div');el.className='page';el.style.width=`${w}px`;el.style.height=`${h}px`;
  const inner=document.createElement('div');inner.className='page-inner';
  const head=document.createElement('div');head.className='running-head';head.textContent=chapter.title;
  const content=document.createElement('div');content.className='page-content';
  const number=document.createElement('div');number.className='page-number';number.textContent='0';inner.append(head,content,number);el.append(inner);return {el,content,number};
}
function currentAnchor(){if(flow)return saved;return pages[flip?.getCurrentPageIndex()??0]?.anchor??saved;}
function paginate(w,h){
  pages=[];const measure=$('measurement');measure.replaceChildren();
  const cover=document.createElement('div');cover.className='page cover';cover.dataset.density='hard';
  cover.innerHTML='<div class="page-inner"><small>DISTRITO 41</small><h2>Caso 001</h2><hr><p>Crônicas de uma guerra</p><div class="edition">HARRY DUBOIS · WAR ERA</div></div>';
  pages.push({el:cover,anchor:{chapter:chapters[0].id,line:-1},chapter:0,cover:true});
  chapters.forEach((chapter,index)=>{
    // Start chapters on a fresh spread so index navigation shows their heading.
    if(pages.length%2===0){const blank=sheet(chapter,w,h);blank.el.classList.add('blank');blank.el.querySelector('.running-head').textContent='Distrito 41';pages.push({...blank,anchor:pages.at(-1).anchor,chapter:Math.max(0,index-1)});}
    let page;
    function fresh(anchor){page=sheet(chapter,w,h);measure.replaceChildren(page.el);pages.push({...page,anchor,chapter:index});}
    fresh({chapter:chapter.id,line:-1});
    for(const block of blocks(chapter)){
      let element=node(block);page.content.append(element);
      if(page.content.scrollHeight<=page.content.clientHeight+1)continue;
      element.remove();
      if(page.content.childNodes.length)fresh({chapter:chapter.id,line:block.line});
      element=node(block);page.content.append(element);
      if(page.content.scrollHeight<=page.content.clientHeight+1)continue;
      element.remove();
      // Split long paragraphs by words, measuring the actual font and viewport.
      const words=block.text.split(/\s+/);let offset=0;
      while(offset<words.length){
        let low=1,high=words.length-offset,best=0;const part=node(block);if(offset)part.classList.add('continued');page.content.append(part);
        while(low<=high){const mid=Math.floor((low+high)/2);part.textContent=words.slice(offset,offset+mid).join(' ');
          if(page.content.scrollHeight<=page.content.clientHeight+1){best=mid;low=mid+1;}else high=mid-1;}
        if(!best)throw new Error('A página ficou pequena demais. Aumente a janela ou use a leitura contínua.');
        part.textContent=words.slice(offset,offset+best).join(' ');offset+=best;
        if(offset<words.length)fresh({chapter:chapter.id,line:block.line,word:offset});
      }
    }
  });
  measure.replaceChildren();
  pages.forEach((page,i)=>{if(page.number)page.number.textContent=String(i);});
}
function locate(anchor){if(!anchor)return 0;let found=0;
  pages.forEach((page,i)=>{if(page.anchor.chapter===anchor.chapter&&page.anchor.line<=anchor.line&&(page.anchor.line<anchor.line||(page.anchor.word??0)<=(anchor.word??0)))found=i;});return found;
}
function update(){if(!flip)return;const i=flip.getCurrentPageIndex(), page=pages[i];if(!page)return;
  saved=page.anchor;storage.set('d41-place',saved);
  document.title=`${page.cover?'Caso 001':chapters[page.chapter].title} · Distrito 41`;
  const pair=flip.getOrientation()==='landscape'&&!page.cover&&i+1<pages.length;
  $('position').textContent=page.cover?'Capa':`Página ${i}${pair?'–'+(i+1):''} de ${pages.length-1}`;
  $('progress').style.width=`${100*i/Math.max(1,pages.length-1)}%`;
  $('previous').disabled=i===0;$('next').disabled=i>=pages.length-(pair?2:1);
  [...$('chapters').children].forEach((button,index)=>button.setAttribute('aria-current',String(index===page.chapter)));
}
function rebuild(anchor=currentAnchor()){
  if(rebuilding||!chapters.length||flow)return;rebuilding=true;
  try{if(flip){flip.destroy();flip=null;}if(!$('book')){const book=document.createElement('div');book.id='book';$('stage').append(book);}
    const {width,height}=dimensions();paginate(width,height);
    flip=new St.PageFlip($('book'),{width,height,size:'fixed',showCover:true,usePortrait:true,flippingTime:matchMedia('(prefers-reduced-motion: reduce)').matches?1:650,maxShadowOpacity:.2,mobileScrollSupport:false,disableFlipByClick:true,startPage:locate(anchor)});
    flip.on('flip',update);flip.on('init',update);flip.on('changeOrientation',update);flip.loadFromHTML(pages.map(p=>p.el));update();$('error').hidden=true;
  }catch(error){$('error').hidden=false;$('error').textContent=`Não consegui abrir as páginas: ${error.message} Você pode usar a leitura contínua.`;}
  finally{rebuilding=false;}
}
function panel(open){$('chapter-panel').hidden=!open;$('contents').setAttribute('aria-expanded',String(open));}
$('contents').onclick=()=>panel($('chapter-panel').hidden);$('close-panel').onclick=()=>panel(false);
$('previous').onclick=()=>flip?.flipPrev();$('next').onclick=()=>flip?.flipNext();
document.addEventListener('keydown',event=>{if(event.key==='Escape')panel(false);if(event.target.closest('input,select,textarea,[contenteditable="true"]')||flow||!$('chapter-panel').hidden||event.altKey||event.ctrlKey||event.metaKey)return;if(event.key==='ArrowRight'){event.preventDefault();flip?.flipNext();}if(event.key==='ArrowLeft'){event.preventDefault();flip?.flipPrev();}});
function fontChange(delta){const anchor=currentAnchor();font=Math.max(15,Math.min(24,font+delta));storage.set('d41-font',font);document.documentElement.style.setProperty('--font',`${font}px`);rebuild(anchor);}
$('smaller').onclick=()=>fontChange(-1);$('larger').onclick=()=>fontChange(1);
$('theme').onclick=()=>{document.body.classList.toggle('night');storage.set('d41-night',document.body.classList.contains('night'));};
$('mode').onclick=()=>{const anchor=currentAnchor();flow=!flow;document.body.classList.toggle('flow',flow);$('stage').hidden=flow;$('continuous').hidden=!flow;$('mode').textContent=flow?'Páginas animadas':'Leitura contínua';if(!flow)rebuild(saved);else document.getElementById(`flow-${anchor?.chapter}`)?.scrollIntoView();};
addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>rebuild(),250);});
async function init(){try{const response=await fetch('/book.json');if(!response.ok)throw new Error('Falha ao carregar capítulos');chapters=await response.json();if(!chapters.length){$('error').hidden=false;$('error').textContent='O novo Distrito 41 está em preparação. Os capítulos aparecerão aqui quando estiverem escritos.';$('stage').hidden=true;$('previous').disabled=true;$('next').disabled=true;return;}
  chapters.forEach((chapter,index)=>{const button=document.createElement('button');button.textContent=chapter.title;button.onclick=()=>{saved={chapter:chapter.id,line:-1};if(flow)document.getElementById(`flow-${chapter.id}`).scrollIntoView();else flip?.turnToPage(locate(saved));storage.set('d41-place',saved);panel(false);};$('chapters').append(button);
    const section=document.createElement('section');section.id=`flow-${chapter.id}`;for(const block of blocks(chapter))section.append(node(block));$('continuous').append(section);
  });await document.fonts.ready;rebuild(saved);
}catch(error){$('error').hidden=false;$('error').textContent=error.message;}}
init();
