from build import AFF_NOTE

JS = r"""
(function(){
function $(s){return document.querySelector(s)}
function f(x){return Math.round(x).toLocaleString('ro-RO')}
var c=$('#calc');if(!c)return;
function run(){var n=+$('#n').value||0,fam=+$('#fam').value||0,stup=+$('#stup').value||0,ech=+$('#ech').value||0,trat=+$('#trat').value||0,kg=+$('#kg').value||0,pr=+$('#pr').value||0,sub=$('#sub').checked;
 var inv=n*(fam+stup)+ech,chelt=n*trat,venit=n*kg*pr,subv=sub?n*15*5.0968:0,profit=venit+subv-chelt;
 $('#rInv').textContent=f(inv)+' lei';$('#rVen').textContent=f(venit)+' lei';$('#rProf').textContent=f(profit)+' lei/an';$('#rPay').textContent=profit>0?(inv/profit).toFixed(1).replace('.',',')+' ani':'—';
 $('#rTab').innerHTML=[['Familii de albine',n*fam],['Stupi echipați',n*stup],['Echipament de bază',ech],['<b>Investiție inițială</b>',inv],['Tratamente, hrană, faguri (pe an)',chelt],['Miere: '+f(n*kg)+' kg × '+pr+' lei',venit],['Sprijin 15 €/familie (dacă se acordă)',subv],['<b>Rezultat anual</b>',profit]].map(function(r){return '<tr><td>'+r[0]+'</td><td class="n">'+f(r[1])+' lei</td></tr>'}).join('')}
c.addEventListener('input',run);c.addEventListener('change',run);run();
})();
"""

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Calculator stupină: investiție, venit și amortizare</h2>
<div class="grid3">
<div><label class="f" for="n">Număr de familii (stupi)</label><input id="n" type="number" min="0" value="20"></div>
<div><label class="f" for="fam">Preț familie de albine / roi (lei)</label><input id="fam" type="number" min="0" value="450"></div>
<div><label class="f" for="stup">Stup echipat (lei/buc.)</label><input id="stup" type="number" min="0" value="550"></div>
<div><label class="f" for="ech">Echipament de bază (lei) <small>centrifugă, costum, afumător, unelte</small></label><input id="ech" type="number" min="0" value="3500"></div>
<div><label class="f" for="trat">Cheltuieli anuale pe stup (lei) <small>tratamente, hrană, faguri</small></label><input id="trat" type="number" min="0" value="90"></div>
<div><label class="f" for="kg">Producție de miere (kg/stup/an)</label><input id="kg" type="number" min="0" value="15"></div>
<div><label class="f" for="pr">Preț de vânzare (lei/kg)</label><input id="pr" type="number" min="0" value="25"></div>
</div>
<label class="chk"><input type="checkbox" id="sub"> Includ sprijinul de 15 €/familie de albine (schema din Legea promulgată în iunie 2026; forma de acordare este în curs de modificare)</label>
<div class="res"><div class="big"><div class="kpi"><span>Investiție inițială</span><b id="rInv">–</b></div><div class="kpi"><span>Venit din miere</span><b id="rVen">–</b></div><div class="kpi main"><span>Rezultat anual</span><b id="rProf">–</b></div><div class="kpi"><span>Amortizare</span><b id="rPay">–</b></div></div>
<div class="tw"><table class="t" id="rTab"></table></div>
<p class="note">Toate valorile sunt editabile: pune prețurile din oferta furnizorului tău și prețul la care vinzi. Producția variază mult de la an la an, cu vremea și cu culesurile din zonă. Nu include munca ta, transportul în pastoral și eventualele pierderi de familii.</p></div></form></div>"""

INDEX_BODY = TOOL + """
<section class="sec"><h2>Apicultura în România, în cifre</h2>
<p>România are aproximativ 2 milioane de stupi și este pe locul doi în Uniunea Europeană după numărul de stupi, după Spania. Sectorul primește anual fonduri europene prin Planul Strategic PAC: pentru 2026, peste 12 milioane de euro, iar pe 12 octombrie 2026 APIA a plătit 51,8 milioane de lei către 5.369 de apicultori.</p>
<div class="box"><b>Pentru 2027: banii se cheltuie din ianuarie.</b> Cheltuielile pentru intervențiile apicole se pot face din 1 ianuarie până la depunerea cererii de plată, iar termenul a fost 31 iulie în 2026. <a href="/sprijin-apicultori-2026.html">Ce se decontează și cum aplici →</a></div></section>
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/sprijin-apicultori-2026.html"><span class="tag">Fonduri</span><b>Sprijin pentru apicultori 2026–2027</b><span>APIA, AFIR și schema de 15 €/familie.</span></a>
<a class="c" href="/cum-incepi-apicultura.html"><span class="tag">Începători</span><b>Cum începi apicultura</b><span>Primul an, echipamentul și greșelile de evitat.</span></a>
<a class="c" href="/stup-dadant-langstroth-layens.html"><span class="tag">Comparație</span><b>Dadant, Langstroth sau Layens?</b><span>Ce tip de stup alegi.</span></a></div></section>"""

FAQ = [
    ('Câți stupi îmi trebuie ca să fie rentabil?', 'Depinde de producție și de cum vinzi. Mulți apicultori încep cu 5–10 familii ca hobby; de la câteva zeci de familii, cu vânzare directă a mierii, activitatea poate deveni o sursă de venit. Pune cifrele tale în calculator.'),
    ('Primesc bani de la stat pentru stupi?', 'Apicultorii înregistrați pot primi decontarea unor cheltuieli prin intervențiile apicole din Planul Strategic PAC, prin APIA. Tinerii apicultori pot accesa și fonduri AFIR pentru instalare. Există și o schemă de 15 euro pe familie de albine, a cărei formă de acordare este în curs de modificare.'),
    ('Pot ține stupi în curte?', 'Da, cu respectarea distanțelor față de vecini și drumuri stabilite de lege și de regulamentele locale și cu înregistrarea stupinei. Întreabă la primărie și la Direcția Sanitar-Veterinară înainte de amplasare.'),
]

ART_SPR = """<p>Apicultura este unul dintre sectoarele agricole cu cele mai multe forme de sprijin. Iată ce există și calendarul la care să fii atent.</p>
<h2>1. Intervențiile apicole prin APIA</h2><p>Prin Planul Strategic PAC 2023–2027, apicultorii individuali și formele asociative (asociații, cooperative) pot primi decontarea unor cheltuieli. Pentru 2026, sectorul a avut un buget de peste 12,16 milioane de euro, finanțat în mod egal de UE și de bugetul de stat.</p>
<ul><li><strong>Ce se decontează:</strong> printre altele, cutii noi de stupi, unelte apicole și echipamente de protecție, echipamente pentru procesarea mierii și medicamente pentru tratarea bolilor (inclusiv varrooza), conform ghidului anual.</li><li><strong>Când cheltui:</strong> cheltuielile sunt eligibile de la 1 ianuarie până la depunerea cererii de plată.</li><li><strong>Termen 2026:</strong> cererile s-au depus până la 31 iulie 2026; APIA a plătit pe 12 octombrie 2026 51,81 milioane de lei către 5.369 de apicultori.</li><li><strong>Cursul de schimb</strong> folosit pentru plățile din 2026: 5,0968 lei/euro.</li></ul>
<p>Pentru 2027, urmărește publicarea noului ghid APIA (de obicei primăvara) și păstrează toate facturile de la 1 ianuarie.</p>
<h2>2. Schema de 15 euro pe familia de albine</h2><p>Președintele a promulgat pe 24 iunie 2026 legea privind o schemă de ajutor de stat de 15 euro pentru fiecare familie de albine, pentru perioada 2026–2028. Ulterior a fost depus un proiect care schimbă mecanismul, transformând sprijinul în ajutor de minimis. Verifică forma finală înainte să te bazezi pe acești bani.</p>
<h2>3. Fonduri AFIR pentru tineri apicultori</h2><p>Prin intervenția DR-30 (instalarea tinerilor fermieri), AFIR a semnat contracte cu 307 tineri apicultori, în valoare de 21,5 milioane de euro. Banii au fost folosiți pentru cutii de stupi, echipamente de extracție și procesare a mierii, unelte și echipamente de protecție.</p>
<h2>Condiții generale</h2><ul><li>Stupii identificați și înregistrați conform reglementărilor sanitar-veterinare și zootehnice.</li><li>Stupina înregistrată și carnet de stupină.</li><li>Pentru unele intervenții, un număr minim de familii.</li></ul>
<div class="box info">Vezi cum schimbă sprijinul rentabilitatea stupinei tale în <a href="/">calculatorul de stupină</a>.</div>"""

ART_INC = """<p>Primul an în apicultură este despre învățat, nu despre profit. Iată cum îl pornești corect.</p>
<h2>1. Învață înainte să cumperi albine</h2><p>Un curs de apicultură (multe asociații județene organizează) și câteva vizite la un apicultor cu experiență valorează mai mult decât orice echipament. Înscrie-te într-o asociație: primești sfaturi, tratamente la preț de grup și acces la programe de sprijin.</p>
<h2>2. Începe cu puține familii</h2><p>Două–cinci familii sunt ideale în primul an: destule ca să compari, puține ca să le poți urmări atent. Cumpără familii sau roiuri de la un apicultor local, sănătoase, cu matcă tânără.</p>
<h2>3. Echipamentul de bază</h2><ul><li>Stupi (alege un singur tip și rămâi la el: <a href="/stup-dadant-langstroth-layens.html">vezi comparația</a>)</li><li>Costum sau bluză cu mască, mănuși</li><li>Afumător și daltă apicolă</li><li>Perie pentru albine</li><li>Hrănitoare</li><li>Centrifugă (poate fi împrumutată în primul an) și bidoane alimentare</li></ul>
<h2>4. Calendarul primului an</h2><ul><li><strong>Primăvara:</strong> instalare, verificarea mătcii, extinderea cuiburilor.</li><li><strong>Vara:</strong> culesuri, prevenirea roitului, extracția mierii.</li><li><strong>După ultimul cules:</strong> tratament împotriva varroa și pregătirea hranei de iarnă.</li><li><strong>Iarna:</strong> liniște; verifici doar din exterior și pregătești echipamentul.</li></ul>
<h2>Greșelile frecvente</h2><ul><li>Tratamentul împotriva varroa făcut prea târziu: cea mai frecventă cauză de pierdere a familiilor.</li><li>Recoltarea întregii miere, fără rezervă pentru iarnă.</li><li>Prea multe tipuri de stupi, cu rame incompatibile.</li></ul>
<p class="note">Respectă legislația sanitar-veterinară: înregistrează stupina, folosește doar tratamente autorizate și ține evidența lor.</p>""" + AFF_NOTE

ART_STUP = """<p>Tipul de stup decide ce rame cumperi, ce centrifugă folosești și cum lucrezi zeci de ani. Iată cele trei variante răspândite.</p>
<h2>Dadant</h2><p>Foarte răspândit în România. Corp mare de cuib, cu magazii mai joase pentru miere. <strong>Plus:</strong> spațiu mare pentru cuib, iernare bună, piese ușor de găsit. <strong>Minus:</strong> corpul cu cuibul este greu.</p>
<h2>Langstroth (multietajat)</h2><p>Corpuri identice, suprapuse. <strong>Plus:</strong> piese interschimbabile, potrivit pentru stupărit pastoral și pentru scară mare. <strong>Minus:</strong> mai multă manipulare de corpuri.</p>
<h2>Layens (orizontal)</h2><p>Stup orizontal, cu rame înalte, fără corpuri suprapuse. <strong>Plus:</strong> nu ridici greutăți, potrivit pentru stupine fixe și pentru cine are probleme de spate. <strong>Minus:</strong> mai greu de transportat și extins.</p>
<div class="tw"><table class="t"><tr><th>Profil</th><th>Recomandare</th></tr><tr><td>Începător, stupină fixă</td><td>Dadant sau Layens</td></tr><tr><td>Pastoral, scară mare</td><td>Langstroth</td></tr><tr><td>Nu vrei să ridici greutăți</td><td>Layens</td></tr></table></div>
<h2>Materialul</h2><p>Lemnul rămâne standardul; stupii din polistiren de densitate mare izolează mai bine, dar verifică regulile pentru apicultura ecologică dacă vrei certificare.</p>
<p>Indiferent de tip, alege un singur standard de ramă pentru toată stupina.</p>""" + AFF_NOTE

SITE = {
    'name': 'StupulModern', 'domain': 'stupulmodern.online',
    'c1': '#8a5a00', 'c2': '#d99a00', 'accent': '#3d2b1f',
    'mark': '<path d="M32 10l18 10v22L32 54 14 42V20z" fill="#fff"/><path d="M32 22l9 5v10l-9 5-9-5V27z" fill="#d99a00"/>',
    'tagline': 'Apicultură practică în România: calcule de rentabilitate, fonduri pentru apicultori și ghiduri pentru începători.',
    'badges': ['Calculator stupină', 'Fonduri APIA și AFIR', 'Ghid începători'],
    'nav': [('/', 'Calculator'), ('/sprijin-apicultori-2026.html', 'Fonduri'), ('/cum-incepi-apicultura.html', 'Începători'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Calculator rentabilitate stupină',
    'side_title': 'E rentabilă stupina ta?', 'side_text': 'Investiție, venit și amortizare, cu cifrele tale.',
    'about': '<p>StupulModern este un site independent pentru apicultorii din România, de la începători la stupine de câteva sute de familii: calcule, fonduri și ghiduri practice.</p><h2>Sursele noastre</h2><p>Comunicatele și ghidurile APIA și AFIR, legislația publicată în Monitorul Oficial și informațiile asociațiilor de apicultori.</p><p>Unele linkuri către magazine pot fi de afiliere și sunt marcate.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Calculator stupină: investiție, venit și amortizare', 'kind': 'tool', 'short': 'Calculator stupină', 'appcat': 'BusinessApplication',
         'desc': 'Calculează investiția într-o stupină, venitul din miere, rezultatul anual și amortizarea. Plus fondurile pentru apicultori în 2026–2027.',
         'h1': 'Calculator stupină: merită să faci apicultură?', 'toolname': 'Calculator rentabilitate stupină',
         'lead': 'Câte familii, ce costuri și la ce preț vinzi mierea: afli investiția, rezultatul anual și în cât timp își scoate banii stupina.', 'body': INDEX_BODY, 'faq': FAQ},
        {'slug': 'sprijin-apicultori-2026', 'title': 'Sprijin pentru apicultori 2026–2027: APIA, AFIR, 15 €/familie', 'kind': 'article', 'short': 'Fonduri pentru apicultori',
         'desc': 'Ce fonduri există pentru apicultori: intervențiile apicole APIA (12 mil. € în 2026), sprijinul AFIR pentru tineri și schema de 15 € pe familia de albine.',
         'h1': 'Sprijin pentru apicultori în 2026–2027', 'lead': 'Ce se decontează, termenele și condițiile, într-un singur loc.', 'body': ART_SPR},
        {'slug': 'cum-incepi-apicultura', 'title': 'Cum începi apicultura: ghid pentru primul an', 'kind': 'article', 'short': 'Cum începi apicultura',
         'desc': 'Ghid pentru începători în apicultură: cu câte familii începi, echipamentul de bază, calendarul primului an și greșelile care costă familii de albine.',
         'h1': 'Cum începi apicultura: primul an', 'lead': 'Pașii, echipamentul și greșelile de evitat în primul sezon.', 'body': ART_INC},
        {'slug': 'stup-dadant-langstroth-layens', 'title': 'Stup Dadant, Langstroth sau Layens: ce alegi?', 'kind': 'article', 'short': 'Dadant, Langstroth sau Layens',
         'desc': 'Comparație între stupii Dadant, Langstroth și Layens: avantaje, dezavantaje și ce tip se potrivește stupinei tale.',
         'h1': 'Dadant, Langstroth sau Layens: ce stup alegi', 'lead': 'Cele trei tipuri de stup, comparate pentru începători și profesioniști.', 'body': ART_STUP},
    ]
}
