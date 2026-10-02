import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const projectDir = path.resolve(process.argv[2] || path.join(import.meta.dirname, '..'));
const skillDir = 'C:/Users/Arifiansyah/.codex/plugins/cache/openai-primary-runtime/presentations/26.904.11930/skills/presentations';
const buildDir = path.join(projectDir, '.build');
const outputDir = path.join(projectDir, 'output');
const draftPath = path.join(buildDir, 'rumah-konsep-draft.pptx');
const finalPath = path.join(outputDir, 'presentasi-desain-elegan-8x18.pptx');
await fs.mkdir(buildDir, { recursive: true });
await fs.mkdir(outputDir, { recursive: true });

const { resolvePresentationFont, finalizePresentation } = await import(
  pathToFileURL(path.join(skillDir, 'container_tools/artifact_tool_utils.mjs')).href,
);
const fontFamily = resolvePresentationFont({ fontFamily: 'Arial' });
const deck = Presentation.create({ slideSize: { width: 1280, height: 720 } });
const C = { ink:'#26312d', muted:'#69756d', cream:'#f5f2eb', paper:'#fffdf8', sage:'#536f5f', rust:'#ae674b', line:'#d9d5ca', pale:'#e9e4d9' };
const px = 1;

function rect(slide, name, x, y, w, h, fill, line='none') {
  return slide.shapes.add({ geometry:'rect', name, position:{left:x,top:y,width:w,height:h}, fill,
    line:{style:'solid',fill:line,width:line==='none'?0:1} });
}
function text(slide, name, str, x, y, w, h, opts={}) {
  const shape=slide.shapes.add({geometry:'textbox',name,position:{left:x,top:y,width:w,height:h},fill:'none',line:{style:'solid',fill:'none',width:0}});
  shape.text=str;
  shape.text.style={typeface:fontFamily,fontSize:opts.size||22,bold:opts.bold||false,color:opts.color||C.ink,
    alignment:opts.align||'left',verticalAlignment:opts.valign||'middle',wrap:true,autoFit:'shrinkText'};
  return shape;
}
async function bytes(rel){return new Uint8Array(await fs.readFile(path.join(projectDir,rel)));}
async function img(slide,rel,name,x,y,w,h,fit='contain'){
  return slide.images.add({blob:await bytes(rel),contentType:'image/png',alt:name,fit,position:{left:x,top:y,width:w,height:h}});
}
function base(slide, number, section){
  slide.background.fill=C.cream;
  rect(slide,`top-rule-${number}`,72,48,34,3,C.rust);
  text(slide,`section-${number}`,section.toUpperCase(),120,35,650,24,{size:13,bold:true,color:C.muted});
  text(slide,`page-${number}`,String(number).padStart(2,'0'),1160,661,48,24,{size:13,color:C.muted,align:'right'});
}
function title(slide,str,sub=''){
  text(slide,'slide-title',str,72,76,1120,62,{size:50,bold:true});
  if(sub) text(slide,'slide-subtitle',sub,74,139,1100,36,{size:20,color:C.muted});
}
function notes(slide,str){slide.speakerNotes.textFrame.setText(str);}
function paragraph(slide,heading,body,x,y,w,headingColor=C.sage){
  text(slide,`heading-${heading}`,heading,x,y,w,30,{size:22,bold:true,color:headingColor});
  text(slide,`body-${heading}`,body,x,y+34,w,80,{size:18,color:C.muted,valign:'top'});
}

// 1 — Cover
{
  const s=deck.slides.add();s.background.fill=C.cream;
  await img(s,'assets/renders/full-house.png','Model rumah dua lantai dengan atap',330,0,950,720,'cover');
  rect(s,'cover-wash',0,0,512,720,C.cream);
  rect(s,'cover-accent',72,82,44,4,C.rust);
  text(s,'cover-kicker','KONSEP HUNIAN · 2026',72,105,360,26,{size:14,bold:true,color:C.sage});
  text(s,'cover-title','Desain elegan\nrumah kekinian',72,184,480,176,{size:54,bold:true});
  text(s,'cover-measure','8 × 18 m',72,399,390,61,{size:45,bold:false,color:C.rust});
  text(s,'cover-subtitle','Studi tata ruang dua lantai\nuntuk kebutuhan keluarga',74,480,376,78,{size:22,color:C.muted,valign:'top'});
  text(s,'cover-footer','DENAH AWAL · MODEL 3D · CATATAN PENGEMBANGAN',74,654,440,24,{size:11,bold:true,color:C.muted});
  notes(s,'Konsep dikembangkan dari sketsa lantai 1 dan daftar kebutuhan ruang lantai 2. Semua dimensi dan susunan ruang masih perkiraan.');
}

// 2 — Program and organizing logic
{
  const s=deck.slides.add();base(s,2,'Program ruang');title(s,'Kebutuhan ruang keluarga','Lantai atas menambah balkon, ruang kerja, dan kamar anak di atas tapak 8 × 18 m.');
  rect(s,'column-rule',639,220,1,354,C.line);
  text(s,'f1-label','01  /  LANTAI 1',74,226,500,25,{size:14,bold:true,color:C.rust});
  text(s,'f1-main','Area komunal dan servis',74,268,500,42,{size:30,bold:true});
  paragraph(s,'Depan','Teras dan ruang tamu menjadi area penerima, dilanjutkan ke ruang keluarga.',74,335,495);
  paragraph(s,'Privat','Kamar 1, kamar 2, dan kamar utama tersusun dari tengah ke belakang.',74,443,495);
  paragraph(s,'Servis','Pantry / dapur, meja makan, toilet bersama, dan cuci jemur.',74,551,495);
  text(s,'f2-label','02  /  LANTAI 2',698,226,500,25,{size:14,bold:true,color:C.rust});
  text(s,'f2-main','Ruang keluarga dan kamar',698,268,520,42,{size:30,bold:true});
  paragraph(s,'Balkon dan tamu','Balkon depan terhubung dengan ruang tamu.',698,335,492);
  paragraph(s,'Kerja dan simpan','Meja kerja serta lemari sepatu ditempatkan dekat sirkulasi tangga.',698,443,492);
  paragraph(s,'Kamar keluarga','Kamar utama dengan toilet dalam, dua kamar anak, toilet bersama, area makan, dan pantry.',698,551,492);
  notes(s,'Susunan lantai 1 mengikuti pembacaan sketsa. Sebagian label area dapur dan servis pada sketsa kurang terbaca, sehingga penyebutannya masih interpretasi. Daftar ruang lantai 2 mengikuti kebutuhan yang diberikan.');
}

// 3 — Floor 1 plan
{
  const s=deck.slides.add();base(s,3,'Denah lantai 1');title(s,'Lantai 1','Interpretasi sketsa awal · zona tamu di depan, kamar di tengah, servis di belakang.');
  await img(s,'assets/floor-1.png','Denah lantai 1 ukuran 8 × 18 m',70,188,475,474,'contain');
  rect(s,'plan-divider',584,205,1,390,C.line);
  text(s,'f1-intro','Ruang utama',624,216,530,35,{size:24,bold:true});
  paragraph(s,'Ruang depan','Teras, ruang tamu, dan ruang keluarga.',624,274,536);
  paragraph(s,'Ruang privat','Kamar 1, kamar 2, dan kamar utama dengan toilet dalam.',624,382,536);
  paragraph(s,'Ruang servis','Pantry / dapur, meja makan, toilet bersama, dan area cuci jemur.',624,490,536);
  text(s,'f1-note','Posisi dan ukuran setiap ruang masih perkiraan.',624,610,540,25,{size:14,color:C.rust});
  notes(s,'Denah adalah pembacaan konseptual dari sketsa yang dilampirkan. Label pantry / dapur dan servis merupakan interpretasi, bukan ukuran hasil survei.');
}

// 4 — Floor 2 plan
{
  const s=deck.slides.add();base(s,4,'Denah lantai 2');title(s,'Lantai 2','Kamar anak berdekatan dengan toilet bersama; kamar utama memiliki toilet di dalam.');
  await img(s,'assets/floor-2.png','Denah lantai 2 ukuran 8 × 18 m',70,188,475,474,'contain');
  rect(s,'plan-divider',584,205,1,390,C.line);
  text(s,'f2-intro','Ruang yang diminta',624,216,530,35,{size:24,bold:true});
  paragraph(s,'Balkon dan kerja','Balkon depan, ruang tamu, area meja kerja, dan lemari sepatu.',624,274,536);
  paragraph(s,'Kamar tidur','Kamar utama dengan toilet dalam, kamar anak perempuan dengan ranjang tingkat, dan kamar anak laki-laki.',624,382,536);
  paragraph(s,'Makan dan servis','Toilet bersama, area meja makan, dan pantry.',624,508,536);
  text(s,'f2-note','Akses tangga dan ruang gerak perlu diuji lagi pada ukuran tapak sebenarnya.',624,610,550,25,{size:14,color:C.rust});
  notes(s,'Pembagian dan dimensi ruang lantai 2 dibuat untuk mengakomodasi daftar kebutuhan yang diberikan. Ukuran aktual akan bergantung pada pengukuran tapak, setback, struktur dan bukaan.');
}

// 5 — Three model modes
{
  const s=deck.slides.add();base(s,5,'Model 3D');title(s,'Tiga cara membaca rumah','Model Blender memisahkan rumah utuh, lantai 1 terbuka, dan lantai 2.');
  const cards=[
    {x:72,file:'assets/renders/full-house.png',label:'01  ·  RUMAH UTUH',detail:'Bentuk massa dan atap'},
    {x:474,file:'assets/renders/floor-1.png',label:'02  ·  LANTAI 1',detail:'Bidang atas disembunyikan'},
    {x:876,file:'assets/renders/floor-2.png',label:'03  ·  LANTAI 2',detail:'Kamar dan ruang atas'},
  ];
  for(const card of cards){
    await img(s,card.file,card.label,card.x,208,332,355,'contain');
    text(s,`label-${card.x}`,card.label,card.x,578,332,25,{size:14,bold:true,color:C.sage});
    text(s,`detail-${card.x}`,card.detail,card.x,607,332,29,{size:18,color:C.muted});
  }
  notes(s,'Tampilan diambil dari model Blender konseptual yang dapat diputar pada halaman web. Render ini membantu melihat hubungan massa dan susunan ruang, bukan representasi kondisi terbangun.');
}

// 6 — Refinement notes
{
  const s=deck.slides.add();base(s,6,'Catatan pengembangan');title(s,'Hal yang perlu dipastikan berikutnya','Sebelum denah menjadi gambar kerja, cocokkan konsep dengan tapak dan kebutuhan penghuni.');
  const items=[
    ['01','Ukur lahan dan aturan tapak','Pastikan lebar, panjang, orientasi akses, batas bangunan, dan ketentuan setempat.'],
    ['02','Uji tangga dan sirkulasi','Periksa lebar jalur, posisi pintu, dan kemudahan bergerak di antara ruang.'],
    ['03','Cek cahaya dan udara','Tentukan bukaan luar dan privasi kamar berdasarkan sisi bangunan yang tersedia.'],
    ['04','Koordinasikan ruang basah','Selaraskan posisi toilet, pantry, saluran, dan jalur instalasi antar lantai.'],
  ];
  for(let i=0;i<items.length;i++){
    const [n,h,b]=items[i],col=i%2,row=Math.floor(i/2),x=74+col*590,y=227+row*169;
    text(s,`note-${n}`,n,x,y,52,38,{size:17,bold:true,color:C.rust});
    text(s,`heading-${n}`,h,x+57,y,470,40,{size:25,bold:true});
    text(s,`body-${n}`,b,x+57,y+49,460,77,{size:18,color:C.muted,valign:'top'});
  }
  rect(s,'final-rule',74,594,1080,1,C.line);
  text(s,'final-caveat','Konsep ini adalah dasar diskusi. Ukuran ruang dan detail konstruksi belum diverifikasi.',74,615,1060,36,{size:17,color:C.sage});
  notes(s,'Langkah pengembangan yang disarankan sebelum dibuat gambar kerja. Tidak ada klaim bahwa kebutuhan struktur, aturan setempat, akses darurat atau detail instalasi telah diverifikasi.');
}

const previewDir=path.join(buildDir,'previews');await fs.mkdir(previewDir,{recursive:true});
for(let i=0;i<deck.slides.items.length;i++){
  const slide=deck.slides.items[i];
  const preview=await deck.export({slide,format:'png',scale:1});
  await fs.writeFile(path.join(previewDir,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await preview.arrayBuffer()));
  const layout=await slide.export({format:'layout'});
  await fs.writeFile(path.join(previewDir,`slide-${String(i+1).padStart(2,'0')}.layout.json`),await layout.text());
}
await (await PresentationFile.exportPptx(deck)).save(draftPath);
const result=await finalizePresentation({
  explicitTotalSlideCount:6,
  requiredNativeTableOwnerSlides:[],
  requiredNativeChartOwnerSlides:[],
  workspaceDir:projectDir,
  candidatePath:draftPath,
  finalPath,
  pythonExecutable:'C:/Users/Arifiansyah/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
  integrityValidatorPath:path.join(skillDir,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(skillDir,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
  fontPolicy:{basis:'design',families:[fontFamily]},
  verifyArtifactToolImport:true,
  receiptPath:path.join(buildDir,'presentasi-desain-elegan-8x18.validation.json'),
});
console.log(JSON.stringify({draftPath,finalPath,fontFamily,result},null,2));
