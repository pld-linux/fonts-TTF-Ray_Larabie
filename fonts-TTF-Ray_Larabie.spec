Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Ray'a Larabie
Group:		X11/Fonts

Name:		fonts-TTF-Ray_Larabie
Version:	20020528
Release:	1
License:	freeware
URL:		http://www.larabiefonts.com/
Source0:	http://fonts.theinstallation.org/allfonts.zip
#NoSource:	0
BuildRequires:	ttmkfdir
BuildRequires:	util-linux
BuildRequires:	textutils
BuildRequires:	unzip
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
%description -l pl

%package -n %{name}-pl
Group:		X11/Fonts
Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Ray'a Larabie
Requires(post,postun):fileutils
Requires(post,postun):sed

%description -n %{name}-pl
%description -n %{name}-pl -l pl
Kolekcja darmowych czcionek TTF. W pakiecie tym znajduj± siê czcionki
\ zawieraj±ce kodowanie iso8859-2

%package -n %{name}-plbad
Group:		X11/Fonts
Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Ray'a Larabie
Requires(post,postun):fileutils
Requires(post,postun):sed

%description -n %{name}-plbad
%description -n %{name}-plbad -l pl
Kolekcja darmowych czcionek TTF. W pakiecie tym znajduj± siê czcionki
\ zawieraj±ce kodowanie iso8859-2 ale polskie znaki nie s± wy¶wietlane


%package -n %{name}-other
Group:		X11/Fonts
Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Ray'a Larabie
Requires(post,postun):fileutils
Requires(post,postun):sed

%description -n %{name}-other
%description -n %{name}-other -l pl
Kolekcja darmowych czcionek TTF. W pakiecie tym znajduj± siê czcionki
\ nie zawieraj±ce kodowania iso8859-2

%prep
%setup -q -c -T
unzip %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
#install `/usr/bin/ttmkfdir |grep iso8859-2 |sed -e 's/.TTF[^;]\+/.TTF/'` \
#$RPM_BUILD_ROOT%{ttffontsdir}/
#cd $RPM_BUILD_ROOT%{ttffontsdir}
#/usr/bin/ttmkfdir |tail +2 >fonts.scale.%{name}
#cd -
#rm -f `/usr/bin/ttmkfdir |grep iso8859-2 |sed -e 's/.TTF[^;]\+/.TTF/'`
install -d $RPM_BUILD_ROOT/sort
install ASTRONBI.TTF $RPM_BUILD_ROOT/sort/
install ASTRONBO.TTF $RPM_BUILD_ROOT/sort/
install ASTRONBV.TTF $RPM_BUILD_ROOT/sort/
install ASTRONBW.TTF $RPM_BUILD_ROOT/sort/
install BERYLIBI.TTF $RPM_BUILD_ROOT/sort/
install BERYLIUB.TTF $RPM_BUILD_ROOT/sort/
install BERYLIUI.TTF $RPM_BUILD_ROOT/sort/
install BERYLIUM.TTF $RPM_BUILD_ROOT/sort/
install BLUEBOLD.TTF $RPM_BUILD_ROOT/sort/
install BLUECOND.TTF $RPM_BUILD_ROOT/sort/
install BLUEHIGH.TTF $RPM_BUILD_ROOT/sort/
install BLUEHIGL.TTF $RPM_BUILD_ROOT/sort/
install BULLPEN3.TTF $RPM_BUILD_ROOT/sort/
install BULLPENI.TTF $RPM_BUILD_ROOT/sort/
install BULLPEN_.TTF $RPM_BUILD_ROOT/sort/
install COLOURBA.TTF $RPM_BUILD_ROOT/sort/
install COLOURBB.TTF $RPM_BUILD_ROOT/sort/
install EDMUNDIS.TTF $RPM_BUILD_ROOT/sort/
install EDMUNDS.TTF $RPM_BUILD_ROOT/sort/
install ENGEBOIT.TTF $RPM_BUILD_ROOT/sort/
install ENGEBOLD.TTF $RPM_BUILD_ROOT/sort/
install ENGEEXBI.TTF $RPM_BUILD_ROOT/sort/
install ENGEEXBO.TTF $RPM_BUILD_ROOT/sort/
install ENGEEXIT.TTF $RPM_BUILD_ROOT/sort/
install ENGEEXPA.TTF $RPM_BUILD_ROOT/sort/
install ENGEITAL.TTF $RPM_BUILD_ROOT/sort/
install ENGEREGU.TTF $RPM_BUILD_ROOT/sort/
install GUANINE_.TTF $RPM_BUILD_ROOT/sort/
install GUNPLAY3.TTF $RPM_BUILD_ROOT/sort/
install GUNPLAY.TTF $RPM_BUILD_ROOT/sort/
install JOYCIRCU.TTF $RPM_BUILD_ROOT/sort/
install KIRSTYBI.TTF $RPM_BUILD_ROOT/sort/
install KIRSTY_B.TTF $RPM_BUILD_ROOT/sort/
install KIRSTYIN.TTF $RPM_BUILD_ROOT/sort/
install KIRSTY_I.TTF $RPM_BUILD_ROOT/sort/
install KIRSTY__.TTF $RPM_BUILD_ROOT/sort/
install MUFFERAW.TTF $RPM_BUILD_ROOT/sort/
install NASALIZA.TTF $RPM_BUILD_ROOT/sort/
install PAKENHAM.TTF $RPM_BUILD_ROOT/sort/
install PRICEDOW.TTF $RPM_BUILD_ROOT/sort/
install PUPCAT__.TTF $RPM_BUILD_ROOT/sort/
install RINA.TTF $RPM_BUILD_ROOT/sort/
install STASMIC_.TTF $RPM_BUILD_ROOT/sort/
install STEELFIB.TTF $RPM_BUILD_ROOT/sort/
install STEELFIS.TTF $RPM_BUILD_ROOT/sort/
install STRENUOU.TTF $RPM_BUILD_ROOT/sort/
install SUBPEAR_.TTF $RPM_BUILD_ROOT/sort/
install TEENBDIT.TTF $RPM_BUILD_ROOT/sort/
install TEENBOLD.TTF $RPM_BUILD_ROOT/sort/
install TEENITAL.TTF $RPM_BUILD_ROOT/sort/
install TEENLITA.TTF $RPM_BUILD_ROOT/sort/
install TEENLITE.TTF $RPM_BUILD_ROOT/sort/
install TEEN____.TTF $RPM_BUILD_ROOT/sort/
install VAHIKAB.TTF $RPM_BUILD_ROOT/sort/
install VAHIKAC.TTF $RPM_BUILD_ROOT/sort/
install VAHIKAI.TTF $RPM_BUILD_ROOT/sort/
install VAHIKA_.TTF $RPM_BUILD_ROOT/sort/
install VECTROID.TTF $RPM_BUILD_ROOT/sort/
install VELVENDA.TTF $RPM_BUILD_ROOT/sort/
install ZEKTONBI.TTF $RPM_BUILD_ROOT/sort/
install ZEKTONBO.TTF $RPM_BUILD_ROOT/sort/
install ZEKTONIT.TTF $RPM_BUILD_ROOT/sort/
install ZEKTON__.TTF $RPM_BUILD_ROOT/sort/

cd $RPM_BUILD_ROOT/sort
/usr/bin/ttmkfdir |tail +2 >fonts.scale.%{name}-pl
cd -

install -d $RPM_BUILD_ROOT%{ttffontsdir}

mv $RPM_BUILD_ROOT/sort/* $RPM_BUILD_ROOT%{ttffontsdir}/
rm -f $RPM_BUILD_ROOT/sort/*

install 20THBOLD.TTF $RPM_BUILD_ROOT/sort/
install 20THBOLI.TTF $RPM_BUILD_ROOT/sort/
install 20THFONT.TTF $RPM_BUILD_ROOT/sort/
install 20THITAL.TTF $RPM_BUILD_ROOT/sort/
install ALMONTE.TTF $RPM_BUILD_ROOT/sort/
install AMERP___.TTF $RPM_BUILD_ROOT/sort/
install ANGLEPOI.TTF $RPM_BUILD_ROOT/sort/
install ANGOSTUB.TTF $RPM_BUILD_ROOT/sort/
install ANGOSTUR.TTF $RPM_BUILD_ROOT/sort/
install AXAXAX.TTF $RPM_BUILD_ROOT/sort/
install BALCONYA.TTF $RPM_BUILD_ROOT/sort/
install BALTAR.TTF $RPM_BUILD_ROOT/sort/
install BIOHP___.TTF $RPM_BUILD_ROOT/sort/
install BORG9.TTF $RPM_BUILD_ROOT/sort/
install BRITP___.TTF $RPM_BUILD_ROOT/sort/
install BUTTERBE.TTF $RPM_BUILD_ROOT/sort/
install CANAP___.TTF $RPM_BUILD_ROOT/sort/
install CAPACITR.TTF $RPM_BUILD_ROOT/sort/
install CARBONBL.TTF $RPM_BUILD_ROOT/sort/
install CARBONPH.TTF $RPM_BUILD_ROOT/sort/
install CHARLESI.TTF $RPM_BUILD_ROOT/sort/
install CHINESER.TTF $RPM_BUILD_ROOT/sort/
install CHRIP___.TTF $RPM_BUILD_ROOT/sort/
install COLAP___.TTF $RPM_BUILD_ROOT/sort/
install CONTOURG.TTF $RPM_BUILD_ROOT/sort/
install COOLVETI.TTF $RPM_BUILD_ROOT/sort/
install CRANBERR.TTF $RPM_BUILD_ROOT/sort/
install CRAPOLA.TTF $RPM_BUILD_ROOT/sort/
install DAZZLESH.TTF $RPM_BUILD_ROOT/sort/
install DENSMORE.TTF $RPM_BUILD_ROOT/sort/
install DIENASTY.TTF $RPM_BUILD_ROOT/sort/
install DIGNITY.TTF $RPM_BUILD_ROOT/sort/
install DROID___.TTF $RPM_BUILD_ROOT/sort/
install DROID.TTF $RPM_BUILD_ROOT/sort/
install ECHECI__.TTF $RPM_BUILD_ROOT/sort/
install ECHEC___.TTF $RPM_BUILD_ROOT/sort/
install ECHEI___.TTF $RPM_BUILD_ROOT/sort/
install ECHELON_.TTF $RPM_BUILD_ROOT/sort/
install ECHELON.TTF $RPM_BUILD_ROOT/sort/
install EFFLANTI.TTF $RPM_BUILD_ROOT/sort/
install EFFLBI__.TTF $RPM_BUILD_ROOT/sort/
install EFFLB___.TTF $RPM_BUILD_ROOT/sort/
install EFFLI___.TTF $RPM_BUILD_ROOT/sort/
install EFFLORES.TTF $RPM_BUILD_ROOT/sort/
install EMBARGO.TTF $RPM_BUILD_ROOT/sort/
install ENDLESS.TTF $RPM_BUILD_ROOT/sort/
install ETHNOCEN.TTF $RPM_BUILD_ROOT/sort/
install EUPHORIG.TTF $RPM_BUILD_ROOT/sort/
install FAILED.TTF $RPM_BUILD_ROOT/sort/
install FIRSTBLI.TTF $RPM_BUILD_ROOT/sort/
install FRENP___.TTF $RPM_BUILD_ROOT/sort/
install GERMP___.TTF $RPM_BUILD_ROOT/sort/
install GHOSTMEA.TTF $RPM_BUILD_ROOT/sort/
install GUMTUCKE.TTF $RPM_BUILD_ROOT/sort/
install HEBRP___.TTF $RPM_BUILD_ROOT/sort/
install HECK.TTF $RPM_BUILD_ROOT/sort/
install HEMIHEAD.TTF $RPM_BUILD_ROOT/sort/
install HIPPP___.TTF $RPM_BUILD_ROOT/sort/
install IRISP___.TTF $RPM_BUILD_ROOT/sort/
install JOYSTIX.TTF $RPM_BUILD_ROOT/sort/
install KENYAN.TTF $RPM_BUILD_ROOT/sort/
install KENYCBI_.TTF $RPM_BUILD_ROOT/sort/
install KENYCB__.TTF $RPM_BUILD_ROOT/sort/
install KENYCI__.TTF $RPM_BUILD_ROOT/sort/
install KENYC___.TTF $RPM_BUILD_ROOT/sort/
install KLEPTOCR.TTF $RPM_BUILD_ROOT/sort/
install KNUCKLED.TTF $RPM_BUILD_ROOT/sort/
install LADYSTAR.TTF $RPM_BUILD_ROOT/sort/
install LESSERCO.TTF $RPM_BUILD_ROOT/sort/
install MAILRAYS.TTF $RPM_BUILD_ROOT/sort/
install MINISYST.TTF $RPM_BUILD_ROOT/sort/
install MINYNBI_.TTF $RPM_BUILD_ROOT/sort/
install MINYNB__.TTF $RPM_BUILD_ROOT/sort/
install MINYNI__.TTF $RPM_BUILD_ROOT/sort/
install MINYN___.TTF $RPM_BUILD_ROOT/sort/
install MONOFONT.TTF $RPM_BUILD_ROOT/sort/
install NAFTA.TTF $RPM_BUILD_ROOT/sort/
install NEURPOLI.TTF $RPM_BUILD_ROOT/sort/
install OLIVERSB.TTF $RPM_BUILD_ROOT/sort/
install ORANGEKI.TTF $RPM_BUILD_ROOT/sort/
install PLAI1978.TTF $RPM_BUILD_ROOT/sort/
install PLASMATI.TTF $RPM_BUILD_ROOT/sort/
install PORTCREB.TTF $RPM_BUILD_ROOT/sort/
install PORTCRED.TTF $RPM_BUILD_ROOT/sort/
install PRESGRG.TTF $RPM_BUILD_ROOT/sort/
install PRIMA___.TTF $RPM_BUILD_ROOT/sort/
install QSWITCHA.TTF $RPM_BUILD_ROOT/sort/
install QUADAPTO.TTF $RPM_BUILD_ROOT/sort/
install RADIOSTA.TTF $RPM_BUILD_ROOT/sort/
install RADIP___.TTF $RPM_BUILD_ROOT/sort/
install SATAP___.TTF $RPM_BUILD_ROOT/sort/
install SAVEDBYZ.TTF $RPM_BUILD_ROOT/sort/
install SPONGY.TTF $RPM_BUILD_ROOT/sort/
install SYBIG___.TTF $RPM_BUILD_ROOT/sort/
install TURKP___.TTF $RPM_BUILD_ROOT/sort/
install TYPODERM.TTF $RPM_BUILD_ROOT/sort/
install UNIONCIT.TTF $RPM_BUILD_ROOT/sort/
install UNISBI__.TTF $RPM_BUILD_ROOT/sort/
install UNISB___.TTF $RPM_BUILD_ROOT/sort/
install UNISI___.TTF $RPM_BUILD_ROOT/sort/
install UNISPACE.TTF $RPM_BUILD_ROOT/sort/
install VIPNAGOR.TTF $RPM_BUILD_ROOT/sort/
install ZEROTWOS.TTF $RPM_BUILD_ROOT/sort/
install ZRNIC___.TTF $RPM_BUILD_ROOT/sort/

cd $RPM_BUILD_ROOT/sort
/usr/bin/ttmkfdir |tail +2 >fonts.scale.%{name}-plbad
cd -

mv $RPM_BUILD_ROOT/sort/* $RPM_BUILD_ROOT%{ttffontsdir}/
rm -f $RPM_BUILD_ROOT/sort/*

install -d $RPM_BUILD_ROOT/sort
install 1980PORT.TTF $RPM_BUILD_ROOT/sort/
install 256BYTES.TTF $RPM_BUILD_ROOT/sort/
install 6809CHAR.TTF $RPM_BUILD_ROOT/sort/
install ABANDONE.TTF $RPM_BUILD_ROOT/sort/
install ABBERANC.TTF $RPM_BUILD_ROOT/sort/
install ADRIATOR.TTF $RPM_BUILD_ROOT/sort/
install AIRCUT.TTF $RPM_BUILD_ROOT/sort/
install AIRMOLEA.TTF $RPM_BUILD_ROOT/sort/
install AIRMOLEQ.TTF $RPM_BUILD_ROOT/sort/
install AIRMOLES.TTF $RPM_BUILD_ROOT/sort/
install AIRMOLE.TTF $RPM_BUILD_ROOT/sort/
install ALIANNA.TTF $RPM_BUILD_ROOT/sort/
install ALMONTEW.TTF $RPM_BUILD_ROOT/sort/
install ALMOSNOW.TTF $RPM_BUILD_ROOT/sort/
install ANKLEPAN.TTF $RPM_BUILD_ROOT/sort/
install ARNPRIOR.TTF $RPM_BUILD_ROOT/sort/
install BABYJEEP.TTF $RPM_BUILD_ROOT/sort/
install BAILEYSC.TTF $RPM_BUILD_ROOT/sort/
install BARBATRI.TTF $RPM_BUILD_ROOT/sort/
install BAVEUSE3.TTF $RPM_BUILD_ROOT/sort/
install BAVEUSE.TTF $RPM_BUILD_ROOT/sort/
install BEATMYGU.TTF $RPM_BUILD_ROOT/sort/
install BETSY.TTF $RPM_BUILD_ROOT/sort/
install BIOMETRI.TTF $RPM_BUILD_ROOT/sort/
install BIRDLAND.TTF $RPM_BUILD_ROOT/sort/
install BITINGOU.TTF $RPM_BUILD_ROOT/sort/
install BITING.TTF $RPM_BUILD_ROOT/sort/
install BLUEHIGB.TTF $RPM_BUILD_ROOT/sort/
install BLUEHIGC.TTF $RPM_BUILD_ROOT/sort/
install BLUEHIGD.TTF $RPM_BUILD_ROOT/sort/
install BORON2.TTF $RPM_BUILD_ROOT/sort/
install BORON.TTF $RPM_BUILD_ROOT/sort/
install BRAESIDE.TTF $RPM_BUILD_ROOT/sort/
install BRAMALEA.TTF $RPM_BUILD_ROOT/sort/
install BUDMOB.TTF $RPM_BUILD_ROOT/sort/
install BUDMO.TTF $RPM_BUILD_ROOT/sort/
install BURNSTOW.TTF $RPM_BUILD_ROOT/sort/
install CHICKENW.TTF $RPM_BUILD_ROOT/sort/
#install CHR$(32).TTF $RPM_BUILD_ROOT/sort/
install COMMLITY.TTF $RPM_BUILD_ROOT/sort/
install COUNTERS.TTF $RPM_BUILD_ROOT/sort/
install CRACKMAN.TTF $RPM_BUILD_ROOT/sort/
install CREDITRI.TTF $RPM_BUILD_ROOT/sort/
install CREDITVA.TTF $RPM_BUILD_ROOT/sort/
install CREDITVB.TTF $RPM_BUILD_ROOT/sort/
install CREDITVI.TTF $RPM_BUILD_ROOT/sort/
install CREDITVZ.TTF $RPM_BUILD_ROOT/sort/
install CRETINO_.TTF $RPM_BUILD_ROOT/sort/
install CRYSTALR.TTF $RPM_BUILD_ROOT/sort/
install CUOMOTYP.TTF $RPM_BUILD_ROOT/sort/
install DEFTONE.TTF $RPM_BUILD_ROOT/sort/
install DEGRASSI.TTF $RPM_BUILD_ROOT/sort/
install DELTAHEY.TTF $RPM_BUILD_ROOT/sort/
install DELUXEDU.TTF $RPM_BUILD_ROOT/sort/
install DENDRITI.TTF $RPM_BUILD_ROOT/sort/
install DEPORTEE.TTF $RPM_BUILD_ROOT/sort/
install DIRTYDOZ.TTF $RPM_BUILD_ROOT/sort/
install DREAMOBX.TTF $RPM_BUILD_ROOT/sort/
install DREAMORB.TTF $RPM_BUILD_ROOT/sort/
install DREAMORI.TTF $RPM_BUILD_ROOT/sort/
install DREAMORP.TTF $RPM_BUILD_ROOT/sort/
install DUALITY_.TTF $RPM_BUILD_ROOT/sort/
install DYSPEPSI.TTF $RPM_BUILD_ROOT/sort/
install EARWIGFA.TTF $RPM_BUILD_ROOT/sort/
install EDENMB__.TTF $RPM_BUILD_ROOT/sort/
install EDENMI__.TTF $RPM_BUILD_ROOT/sort/
install EDENM___.TTF $RPM_BUILD_ROOT/sort/
install EDGEWATE.TTF $RPM_BUILD_ROOT/sort/
install ELECTBGI.TTF $RPM_BUILD_ROOT/sort/
install ELECTBGU.TTF $RPM_BUILD_ROOT/sort/
install ELECTBLU.TTF $RPM_BUILD_ROOT/sort/
install ELECTROH.TTF $RPM_BUILD_ROOT/sort/
install ENNOBLED.TTF $RPM_BUILD_ROOT/sort/
install EYERHYME.TTF $RPM_BUILD_ROOT/sort/
install FABIAN__.TTF $RPM_BUILD_ROOT/sort/
install FADGOD.TTF $RPM_BUILD_ROOT/sort/
install FAKERECE.TTF $RPM_BUILD_ROOT/sort/
install FIELDDAY.TTF $RPM_BUILD_ROOT/sort/
#install $FIVEDOU.TTF $RPM_BUILD_ROOT/sort/
install FLUORIDE.TTF $RPM_BUILD_ROOT/sort/
install FORGOTBI.TTF $RPM_BUILD_ROOT/sort/
install FORGOTTB.TTF $RPM_BUILD_ROOT/sort/
install FORGOTTE.TTF $RPM_BUILD_ROOT/sort/
install FORGOTTI.TTF $RPM_BUILD_ROOT/sort/
install FORGOTTR.TTF $RPM_BUILD_ROOT/sort/
install FORGOTTS.TTF $RPM_BUILD_ROOT/sort/
install FORGOTTY.TTF $RPM_BUILD_ROOT/sort/
install FRAGILEB.TTF $RPM_BUILD_ROOT/sort/
install FRAK.TTF $RPM_BUILD_ROOT/sort/
install FROZEN.TTF $RPM_BUILD_ROOT/sort/
install GIANTTIG.TTF $RPM_BUILD_ROOT/sort/
install GLAZKRAK.TTF $RPM_BUILD_ROOT/sort/
install GOLDENGI.TTF $RPM_BUILD_ROOT/sort/
install GOODFISB.TTF $RPM_BUILD_ROOT/sort/
install GOODFISC.TTF $RPM_BUILD_ROOT/sort/
install GOODFISH.TTF $RPM_BUILD_ROOT/sort/
install GOODFISI.TTF $RPM_BUILD_ROOT/sort/
install GOODTIME.TTF $RPM_BUILD_ROOT/sort/
install GOTNOHEA.TTF $RPM_BUILD_ROOT/sort/
install GRAFFITI.TTF $RPM_BUILD_ROOT/sort/
install GREENFUZ.TTF $RPM_BUILD_ROOT/sort/
install GROOVYGH.TTF $RPM_BUILD_ROOT/sort/
install GYPARODY.TTF $RPM_BUILD_ROOT/sort/
install GYRUSSIA.TTF $RPM_BUILD_ROOT/sort/
install HAMMAMAM.TTF $RPM_BUILD_ROOT/sort/
install HAWKEYE_.TTF $RPM_BUILD_ROOT/sort/
install HAWKEYE.TTF $RPM_BUILD_ROOT/sort/
install HEAVYHEA.TTF $RPM_BUILD_ROOT/sort/
install HELLOLAR.TTF $RPM_BUILD_ROOT/sort/
install HOLYSMOK.TTF $RPM_BUILD_ROOT/sort/
install HOMESWEE.TTF $RPM_BUILD_ROOT/sort/
install HOOKEDON.TTF $RPM_BUILD_ROOT/sort/
install HOOKED.TTF $RPM_BUILD_ROOT/sort/
install HORSPOWR.TTF $RPM_BUILD_ROOT/sort/
install HOTS.TTF $RPM_BUILD_ROOT/sort/
install HURONTAR.TTF $RPM_BUILD_ROOT/sort/
install HURRYUP.TTF $RPM_BUILD_ROOT/sort/
install HUSKYSTA.TTF $RPM_BUILD_ROOT/sort/
install HYDROGEN.TTF $RPM_BUILD_ROOT/sort/
install ICICLECO.TTF $RPM_BUILD_ROOT/sort/
install INDUCTIO.TTF $RPM_BUILD_ROOT/sort/
install INFLAMMA.TTF $RPM_BUILD_ROOT/sort/
install INSTANTT.TTF $RPM_BUILD_ROOT/sort/
install INTERPLA.TTF $RPM_BUILD_ROOT/sort/
install IOMANOID.TTF $RPM_BUILD_ROOT/sort/
install JIGSAWTR.TTF $RPM_BUILD_ROOT/sort/
install JINGOPOP.TTF $RPM_BUILD_ROOT/sort/
install JOHNNYFE.TTF $RPM_BUILD_ROOT/sort/
install KARMASUT.TTF $RPM_BUILD_ROOT/sort/
install KICKINGL.TTF $RPM_BUILD_ROOT/sort/
install KIMBERLE.TTF $RPM_BUILD_ROOT/sort/
install KINGRICH.TTF $RPM_BUILD_ROOT/sort/
install KINGRICI.TTF $RPM_BUILD_ROOT/sort/
install KREDIT1.TTF $RPM_BUILD_ROOT/sort/
install KUSTOMKA.TTF $RPM_BUILD_ROOT/sort/
install LARABIEB.TTF $RPM_BUILD_ROOT/sort/
install LARABIEF.TTF $RPM_BUILD_ROOT/sort/
#install LET'SEAT.TTF $RPM_BUILD_ROOT/sort/
install LETTERA.TTF $RPM_BUILD_ROOT/sort/
install LETTERB.TTF $RPM_BUILD_ROOT/sort/
install LETTERC.TTF $RPM_BUILD_ROOT/sort/
install LEWINSKY.TTF $RPM_BUILD_ROOT/sort/
install LIBEL.TTF $RPM_BUILD_ROOT/sort/
install LILLIPUT.TTF $RPM_BUILD_ROOT/sort/
install LIVINGBY.TTF $RPM_BUILD_ROOT/sort/
install LOCKERGN.TTF $RPM_BUILD_ROOT/sort/
install LUCKYAPE.TTF $RPM_BUILD_ROOT/sort/
install LUNASEQU.TTF $RPM_BUILD_ROOT/sort/
install LUNASOL.TTF $RPM_BUILD_ROOT/sort/
install LUNAUROR.TTF $RPM_BUILD_ROOT/sort/
install LUNECLPS.TTF $RPM_BUILD_ROOT/sort/
install MAITAI.TTF $RPM_BUILD_ROOT/sort/
install MALACHE.TTF $RPM_BUILD_ROOT/sort/
install MAPOFYOU.TTF $RPM_BUILD_ROOT/sort/
install MARQUEEM.TTF $RPM_BUILD_ROOT/sort/
install MASSIVER.TTF $RPM_BUILD_ROOT/sort/
install METALORD.TTF $RPM_BUILD_ROOT/sort/
install MEXCEL3D.TTF $RPM_BUILD_ROOT/sort/
install MEXCELLE.TTF $RPM_BUILD_ROOT/sort/
install MINYA.TTF $RPM_BUILD_ROOT/sort/
install MISIRLOD.TTF $RPM_BUILD_ROOT/sort/
install MISIRLOU.TTF $RPM_BUILD_ROOT/sort/
install MISSISSA.TTF $RPM_BUILD_ROOT/sort/
install MISTERFI.TTF $RPM_BUILD_ROOT/sort/
install MLURMLRY.TTF $RPM_BUILD_ROOT/sort/
install MOBCONCR.TTF $RPM_BUILD_ROOT/sort/
install MODELWOR.TTF $RPM_BUILD_ROOT/sort/
install MOLDPAPA.TTF $RPM_BUILD_ROOT/sort/
install MOTORCAD.TTF $RPM_BUILD_ROOT/sort/
install NASAL.TTF $RPM_BUILD_ROOT/sort/
install NEUROCHR.TTF $RPM_BUILD_ROOT/sort/
install NEUROPOL.TTF $RPM_BUILD_ROOT/sort/
install NEWBRILL.TTF $RPM_BUILD_ROOT/sort/
install NIGHTCOU.TTF $RPM_BUILD_ROOT/sort/
install NIGHTPOR.TTF $RPM_BUILD_ROOT/sort/
install OCTOVILL.TTF $RPM_BUILD_ROOT/sort/
install OPERATIO.TTF $RPM_BUILD_ROOT/sort/
install OUIJADOR.TTF $RPM_BUILD_ROOT/sort/
install OUTRIGHT.TTF $RPM_BUILD_ROOT/sort/
install OVERLOAD.TTF $RPM_BUILD_ROOT/sort/
install PAINTBOY.TTF $RPM_BUILD_ROOT/sort/
install PANTSPAT.TTF $RPM_BUILD_ROOT/sort/
install PARAAMIN.TTF $RPM_BUILD_ROOT/sort/
install PASTOROF.TTF $RPM_BUILD_ROOT/sort/
install PEATLOAF.TTF $RPM_BUILD_ROOT/sort/
install PLAINCRE.TTF $RPM_BUILD_ROOT/sort/
install PLANETBE.TTF $RPM_BUILD_ROOT/sort/
install PLASTICB.TTF $RPM_BUILD_ROOT/sort/
install POBEEF.TTF $RPM_BUILD_ROOT/sort/
install POKE.TTF $RPM_BUILD_ROOT/sort/
install POPUP.TTF $RPM_BUILD_ROOT/sort/
install PRIMEMIN.TTF $RPM_BUILD_ROOT/sort/
install PRIMERB.TTF $RPM_BUILD_ROOT/sort/
install PRIMER.TTF $RPM_BUILD_ROOT/sort/
install PULSESTA.TTF $RPM_BUILD_ROOT/sort/
install PYRITE.TTF $RPM_BUILD_ROOT/sort/
install QUADRANG.TTF $RPM_BUILD_ROOT/sort/
install QUANTITY.TTF $RPM_BUILD_ROOT/sort/
install QUININE.TTF $RPM_BUILD_ROOT/sort/
install QUINOLIN.TTF $RPM_BUILD_ROOT/sort/
install QUINQUEF.TTF $RPM_BUILD_ROOT/sort/
install QUIXOTIC.TTF $RPM_BUILD_ROOT/sort/
install RADIOHAR.TTF $RPM_BUILD_ROOT/sort/
install RADIOSIN.TTF $RPM_BUILD_ROOT/sort/
install RAZORKEE.TTF $RPM_BUILD_ROOT/sort/
install RELISHGA.TTF $RPM_BUILD_ROOT/sort/
install RIOTACT.TTF $RPM_BUILD_ROOT/sort/
install ROBOKOZ.TTF $RPM_BUILD_ROOT/sort/
install ROTHWELL.TTF $RPM_BUILD_ROOT/sort/
install RUSTPROO.TTF $RPM_BUILD_ROOT/sort/
install SADFILMS.TTF $RPM_BUILD_ROOT/sort/
install SANDOVAL.TTF $RPM_BUILD_ROOT/sort/
install SCREENGE.TTF $RPM_BUILD_ROOT/sort/
install SCRITZY.TTF $RPM_BUILD_ROOT/sort/
install SENDCASH.TTF $RPM_BUILD_ROOT/sort/
install SEXSMITH.TTF $RPM_BUILD_ROOT/sort/
install SHIFTY.TTF $RPM_BUILD_ROOT/sort/
install SHLOP___.TTF $RPM_BUILD_ROOT/sort/
install SHLOP.TTF $RPM_BUILD_ROOT/sort/
install SHOULDVE.TTF $RPM_BUILD_ROOT/sort/
install SHOULDVS.TTF $RPM_BUILD_ROOT/sort/
install SILICONC.TTF $RPM_BUILD_ROOT/sort/
install SKELETOR.TTF $RPM_BUILD_ROOT/sort/
install SLOEGIN.TTF $RPM_BUILD_ROOT/sort/
install Snidely.ttf $RPM_BUILD_ROOT/sort/
install SNIDELY_.TTF $RPM_BUILD_ROOT/sort/
install SOFACHRI.TTF $RPM_BUILD_ROOT/sort/
install SOFACHRO.TTF $RPM_BUILD_ROOT/sort/
install SORUNDOW.TTF $RPM_BUILD_ROOT/sort/
install SOULMAMA.TTF $RPM_BUILD_ROOT/sort/
install SOULPAPA.TTF $RPM_BUILD_ROOT/sort/
install SQUEALEM.TTF $RPM_BUILD_ROOT/sort/
install SQUEALER.TTF $RPM_BUILD_ROOT/sort/
install SRSERVIC.TTF $RPM_BUILD_ROOT/sort/
install STEREOFI.TTF $RPM_BUILD_ROOT/sort/
install STILLTIM.TTF $RPM_BUILD_ROOT/sort/
install STITCH.TTF $RPM_BUILD_ROOT/sort/
install STREETCR.TTF $RPM_BUILD_ROOT/sort/
install STUPEFAC.TTF $RPM_BUILD_ROOT/sort/
install STYROFOA.TTF $RPM_BUILD_ROOT/sort/
install SUDBURY3.TTF $RPM_BUILD_ROOT/sort/
install SUDBURY.TTF $RPM_BUILD_ROOT/sort/
install SUIGBI__.TTF $RPM_BUILD_ROOT/sort/
install SUIGB___.TTF $RPM_BUILD_ROOT/sort/
install SUIGENER.TTF $RPM_BUILD_ROOT/sort/
install SUIGI___.TTF $RPM_BUILD_ROOT/sort/
install SUPERGLU.TTF $RPM_BUILD_ROOT/sort/
install SUPERHET.TTF $RPM_BUILD_ROOT/sort/
install SWITCHIN.TTF $RPM_BUILD_ROOT/sort/
install TERYLENE.TTF $RPM_BUILD_ROOT/sort/
install THIAMINE.TTF $RPM_BUILD_ROOT/sort/
install TINSNIPS.TTF $RPM_BUILD_ROOT/sort/
install TOBINTAX.TTF $RPM_BUILD_ROOT/sort/
install TOFU.TTF $RPM_BUILD_ROOT/sort/
install TOMMYGUN.TTF $RPM_BUILD_ROOT/sort/
install TOPBOND.TTF $RPM_BUILD_ROOT/sort/
install TORKBI__.TTF $RPM_BUILD_ROOT/sort/
install TORKB___.TTF $RPM_BUILD_ROOT/sort/
install TORKI___.TTF $RPM_BUILD_ROOT/sort/
install TORK____.TTF $RPM_BUILD_ROOT/sort/
install TRAPPERJ.TTF $RPM_BUILD_ROOT/sort/
install TRIACSEV.TTF $RPM_BUILD_ROOT/sort/
install TROLLBAI.TTF $RPM_BUILD_ROOT/sort/
install UNIVOX.TTF $RPM_BUILD_ROOT/sort/
install UNSTEADY.TTF $RPM_BUILD_ROOT/sort/
install URKELIAN.TTF $RPM_BUILD_ROOT/sort/
install URURMA.TTF $RPM_BUILD_ROOT/sort/
install VADEMECU.TTF $RPM_BUILD_ROOT/sort/
install VANILLA.TTF $RPM_BUILD_ROOT/sort/
install VANISHIN.TTF $RPM_BUILD_ROOT/sort/
install VDUB.TTF $RPM_BUILD_ROOT/sort/
install VENUSRIS.TTF $RPM_BUILD_ROOT/sort/
install VIBROCEB.TTF $RPM_BUILD_ROOT/sort/
install VIBROCEI.TTF $RPM_BUILD_ROOT/sort/
install VIBROCEN.TTF $RPM_BUILD_ROOT/sort/
install VIBROCEX.TTF $RPM_BUILD_ROOT/sort/
install WAKEBAKE.TTF $RPM_BUILD_ROOT/sort/
install WALSHESO.TTF $RPM_BUILD_ROOT/sort/
install WALSHES.TTF $RPM_BUILD_ROOT/sort/
install WEBSTERW.TTF $RPM_BUILD_ROOT/sort/
install WELFAREB.TTF $RPM_BUILD_ROOT/sort/
install WETPET.TTF $RPM_BUILD_ROOT/sort/
install WHITELAK.TTF $RPM_BUILD_ROOT/sort/
install WILDSEWE.TTF $RPM_BUILD_ROOT/sort/
install WINTERMU.TTF $RPM_BUILD_ROOT/sort/
install WORLDOFW.TTF $RPM_BUILD_ROOT/sort/
install WORTHLES.TTF $RPM_BUILD_ROOT/sort/
install XENOWORT.TTF $RPM_BUILD_ROOT/sort/
install XOLTO.TTF $RPM_BUILD_ROOT/sort/
install XTRAFLEX.TTF $RPM_BUILD_ROOT/sort/
install !Y2KBUG.TTF $RPM_BUILD_ROOT/sort/
install YADOU.TTF $RPM_BUILD_ROOT/sort/
install YAWNOVIS.TTF $RPM_BUILD_ROOT/sort/
install YBANDTUN.TTF $RPM_BUILD_ROOT/sort/
install YELLOWPI.TTF $RPM_BUILD_ROOT/sort/
install YONDERRE.TTF $RPM_BUILD_ROOT/sort/
install YOUREGOI.TTF $RPM_BUILD_ROOT/sort/
install YOUREGON.TTF $RPM_BUILD_ROOT/sort/
install YYTRIUMD.TTF $RPM_BUILD_ROOT/sort/
install ZEKTONDO.TTF $RPM_BUILD_ROOT/sort/
install ZEROES__.TTF $RPM_BUILD_ROOT/sort/
install ZEROHOUR.TTF $RPM_BUILD_ROOT/sort/
install ZEROTHRE.TTF $RPM_BUILD_ROOT/sort/
install ZODILLIN.TTF $RPM_BUILD_ROOT/sort/

cd $RPM_BUILD_ROOT/sort
/usr/bin/ttmkfdir |tail +2 >fonts.scale.%{name}-other
cd -

mv $RPM_BUILD_ROOT/sort/* $RPM_BUILD_ROOT%{ttffontsdir}/
rm -f $RPM_BUILD_ROOT/sort/*

#/usr/bin/ttmkfdir |tail +2 >fonts.scale.%{name}-other
#install *.TTF *.ttf fonts.scale.%{name}-other $RPM_BUILD_ROOT%{ttffontsdir}

mv "PASTOR O.TXT" PASTORO.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{name}-pl
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%postun -n %{name}-pl
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%post -n %{name}-plbad
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%postun -n %{name}-plbad
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%post -n %{name}-other
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%postun -n %{name}-other
cd %{ttffontsdir}
umask 022
rm -f fonts.scale.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%files -n %{name}-pl
%defattr(644,root,root,755)
%doc READ_ME.TXT TEEN.TXT
%{ttffontsdir}/fonts.scale.%{name}-pl
%{ttffontsdir}/ASTRONBI.TTF
%{ttffontsdir}/ASTRONBO.TTF
%{ttffontsdir}/ASTRONBV.TTF
%{ttffontsdir}/ASTRONBW.TTF
%{ttffontsdir}/BERYLIBI.TTF
%{ttffontsdir}/BERYLIUB.TTF
%{ttffontsdir}/BERYLIUI.TTF
%{ttffontsdir}/BERYLIUM.TTF
%{ttffontsdir}/BLUEBOLD.TTF
%{ttffontsdir}/BLUECOND.TTF
%{ttffontsdir}/BLUEHIGH.TTF
%{ttffontsdir}/BLUEHIGL.TTF
%{ttffontsdir}/BULLPEN3.TTF
%{ttffontsdir}/BULLPENI.TTF
%{ttffontsdir}/BULLPEN_.TTF
%{ttffontsdir}/COLOURBA.TTF
%{ttffontsdir}/COLOURBB.TTF
%{ttffontsdir}/EDMUNDIS.TTF
%{ttffontsdir}/EDMUNDS.TTF
%{ttffontsdir}/ENGEBOIT.TTF
%{ttffontsdir}/ENGEBOLD.TTF
%{ttffontsdir}/ENGEEXBI.TTF
%{ttffontsdir}/ENGEEXBO.TTF
%{ttffontsdir}/ENGEEXIT.TTF
%{ttffontsdir}/ENGEEXPA.TTF
%{ttffontsdir}/ENGEITAL.TTF
%{ttffontsdir}/ENGEREGU.TTF
%{ttffontsdir}/GUANINE_.TTF
%{ttffontsdir}/GUNPLAY3.TTF
%{ttffontsdir}/GUNPLAY.TTF
%{ttffontsdir}/JOYCIRCU.TTF
%{ttffontsdir}/KIRSTYBI.TTF
%{ttffontsdir}/KIRSTY_B.TTF
%{ttffontsdir}/KIRSTYIN.TTF
%{ttffontsdir}/KIRSTY_I.TTF
%{ttffontsdir}/KIRSTY__.TTF
%{ttffontsdir}/MUFFERAW.TTF
%{ttffontsdir}/NASALIZA.TTF
%{ttffontsdir}/PAKENHAM.TTF
%{ttffontsdir}/PRICEDOW.TTF
%{ttffontsdir}/PUPCAT__.TTF
%{ttffontsdir}/RINA.TTF
%{ttffontsdir}/STASMIC_.TTF
%{ttffontsdir}/STEELFIB.TTF
%{ttffontsdir}/STEELFIS.TTF
%{ttffontsdir}/STRENUOU.TTF
%{ttffontsdir}/SUBPEAR_.TTF
%{ttffontsdir}/TEENBDIT.TTF
%{ttffontsdir}/TEENBOLD.TTF
%{ttffontsdir}/TEENITAL.TTF
%{ttffontsdir}/TEENLITA.TTF
%{ttffontsdir}/TEENLITE.TTF
%{ttffontsdir}/TEEN____.TTF
%{ttffontsdir}/VAHIKAB.TTF
%{ttffontsdir}/VAHIKAC.TTF
%{ttffontsdir}/VAHIKAI.TTF
%{ttffontsdir}/VAHIKA_.TTF
%{ttffontsdir}/VECTROID.TTF
%{ttffontsdir}/VELVENDA.TTF
%{ttffontsdir}/ZEKTONBI.TTF
%{ttffontsdir}/ZEKTONBO.TTF
%{ttffontsdir}/ZEKTONIT.TTF
%{ttffontsdir}/ZEKTON__.TTF

%files -n %{name}-plbad
%defattr(644,root,root,755)
%doc READ_ME.TXT
%{ttffontsdir}/fonts.scale.%{name}-plbad
%{ttffontsdir}/20THBOLD.TTF
%{ttffontsdir}/20THBOLI.TTF
%{ttffontsdir}/20THFONT.TTF
%{ttffontsdir}/20THITAL.TTF
%{ttffontsdir}/ALMONTE.TTF
%{ttffontsdir}/AMERP___.TTF
%{ttffontsdir}/ANGLEPOI.TTF
%{ttffontsdir}/ANGOSTUB.TTF
%{ttffontsdir}/ANGOSTUR.TTF
%{ttffontsdir}/AXAXAX.TTF
%{ttffontsdir}/BALCONYA.TTF
%{ttffontsdir}/BALTAR.TTF
%{ttffontsdir}/BIOHP___.TTF
%{ttffontsdir}/BORG9.TTF
%{ttffontsdir}/BRITP___.TTF
%{ttffontsdir}/BUTTERBE.TTF
%{ttffontsdir}/CANAP___.TTF
%{ttffontsdir}/CAPACITR.TTF
%{ttffontsdir}/CARBONBL.TTF
%{ttffontsdir}/CARBONPH.TTF
%{ttffontsdir}/CHARLESI.TTF
%{ttffontsdir}/CHINESER.TTF
%{ttffontsdir}/CHRIP___.TTF
%{ttffontsdir}/COLAP___.TTF
%{ttffontsdir}/CONTOURG.TTF
%{ttffontsdir}/COOLVETI.TTF
%{ttffontsdir}/CRANBERR.TTF
%{ttffontsdir}/CRAPOLA.TTF
%{ttffontsdir}/DAZZLESH.TTF
%{ttffontsdir}/DENSMORE.TTF
%{ttffontsdir}/DIENASTY.TTF
%{ttffontsdir}/DIGNITY.TTF
%{ttffontsdir}/DROID___.TTF
%{ttffontsdir}/DROID.TTF
%{ttffontsdir}/ECHECI__.TTF
%{ttffontsdir}/ECHEC___.TTF
%{ttffontsdir}/ECHEI___.TTF
%{ttffontsdir}/ECHELON_.TTF
%{ttffontsdir}/ECHELON.TTF
%{ttffontsdir}/EFFLANTI.TTF
%{ttffontsdir}/EFFLBI__.TTF
%{ttffontsdir}/EFFLB___.TTF
%{ttffontsdir}/EFFLI___.TTF
%{ttffontsdir}/EFFLORES.TTF
%{ttffontsdir}/EMBARGO.TTF
%{ttffontsdir}/ENDLESS.TTF
%{ttffontsdir}/ETHNOCEN.TTF
%{ttffontsdir}/EUPHORIG.TTF
%{ttffontsdir}/FAILED.TTF
%{ttffontsdir}/FIRSTBLI.TTF
%{ttffontsdir}/FRENP___.TTF
%{ttffontsdir}/GERMP___.TTF
%{ttffontsdir}/GHOSTMEA.TTF
%{ttffontsdir}/GUMTUCKE.TTF
%{ttffontsdir}/HEBRP___.TTF
%{ttffontsdir}/HECK.TTF
%{ttffontsdir}/HEMIHEAD.TTF
%{ttffontsdir}/HIPPP___.TTF
%{ttffontsdir}/IRISP___.TTF
%{ttffontsdir}/JOYSTIX.TTF
%{ttffontsdir}/KENYAN.TTF
%{ttffontsdir}/KENYCBI_.TTF
%{ttffontsdir}/KENYCB__.TTF
%{ttffontsdir}/KENYCI__.TTF
%{ttffontsdir}/KENYC___.TTF
%{ttffontsdir}/KLEPTOCR.TTF
%{ttffontsdir}/KNUCKLED.TTF
%{ttffontsdir}/LADYSTAR.TTF
%{ttffontsdir}/LESSERCO.TTF
%{ttffontsdir}/MAILRAYS.TTF
%{ttffontsdir}/MINISYST.TTF
%{ttffontsdir}/MINYNBI_.TTF
%{ttffontsdir}/MINYNB__.TTF
%{ttffontsdir}/MINYNI__.TTF
%{ttffontsdir}/MINYN___.TTF
%{ttffontsdir}/MONOFONT.TTF
%{ttffontsdir}/NAFTA.TTF
%{ttffontsdir}/NEURPOLI.TTF
%{ttffontsdir}/OLIVERSB.TTF
%{ttffontsdir}/ORANGEKI.TTF
%{ttffontsdir}/PLAI1978.TTF
%{ttffontsdir}/PLASMATI.TTF
%{ttffontsdir}/PORTCREB.TTF
%{ttffontsdir}/PORTCRED.TTF
%{ttffontsdir}/PRESGRG.TTF
%{ttffontsdir}/PRIMA___.TTF
%{ttffontsdir}/QSWITCHA.TTF
%{ttffontsdir}/QUADAPTO.TTF
%{ttffontsdir}/RADIOSTA.TTF
%{ttffontsdir}/RADIP___.TTF
%{ttffontsdir}/SATAP___.TTF
%{ttffontsdir}/SAVEDBYZ.TTF
%{ttffontsdir}/SPONGY.TTF
%{ttffontsdir}/SYBIG___.TTF
%{ttffontsdir}/TURKP___.TTF
%{ttffontsdir}/TYPODERM.TTF
%{ttffontsdir}/UNIONCIT.TTF
%{ttffontsdir}/UNISBI__.TTF
%{ttffontsdir}/UNISB___.TTF
%{ttffontsdir}/UNISI___.TTF
%{ttffontsdir}/UNISPACE.TTF
%{ttffontsdir}/VIPNAGOR.TTF
%{ttffontsdir}/ZEROTWOS.TTF
%{ttffontsdir}/ZRNIC___.TTF

%files -n %{name}-other
%defattr(644,root,root,755)
%doc READ_ME.TXT BETSY.TXT COUNTERS.TXT PASTORO.TXT
%{ttffontsdir}/fonts.scale.%{name}-other
%{ttffontsdir}/1980PORT.TTF
%{ttffontsdir}/256BYTES.TTF
%{ttffontsdir}/6809CHAR.TTF
%{ttffontsdir}/ABANDONE.TTF
%{ttffontsdir}/ABBERANC.TTF
%{ttffontsdir}/ADRIATOR.TTF
%{ttffontsdir}/AIRCUT.TTF
%{ttffontsdir}/AIRMOLEA.TTF
%{ttffontsdir}/AIRMOLEQ.TTF
%{ttffontsdir}/AIRMOLES.TTF
%{ttffontsdir}/AIRMOLE.TTF
%{ttffontsdir}/ALIANNA.TTF
%{ttffontsdir}/ALMONTEW.TTF
%{ttffontsdir}/ALMOSNOW.TTF
%{ttffontsdir}/ANKLEPAN.TTF
%{ttffontsdir}/ARNPRIOR.TTF
%{ttffontsdir}/BABYJEEP.TTF
%{ttffontsdir}/BAILEYSC.TTF
%{ttffontsdir}/BARBATRI.TTF
%{ttffontsdir}/BAVEUSE3.TTF
%{ttffontsdir}/BAVEUSE.TTF
%{ttffontsdir}/BEATMYGU.TTF
%{ttffontsdir}/BETSY.TTF
%{ttffontsdir}/BIOMETRI.TTF
%{ttffontsdir}/BIRDLAND.TTF
%{ttffontsdir}/BITINGOU.TTF
%{ttffontsdir}/BITING.TTF
%{ttffontsdir}/BLUEHIGB.TTF
%{ttffontsdir}/BLUEHIGC.TTF
%{ttffontsdir}/BLUEHIGD.TTF
%{ttffontsdir}/BORON2.TTF
%{ttffontsdir}/BORON.TTF
%{ttffontsdir}/BRAESIDE.TTF
%{ttffontsdir}/BRAMALEA.TTF
%{ttffontsdir}/BUDMOB.TTF
%{ttffontsdir}/BUDMO.TTF
%{ttffontsdir}/BURNSTOW.TTF
%{ttffontsdir}/CHICKENW.TTF
#%{ttffontsdir}/CHR$(32).TTF
%{ttffontsdir}/COMMLITY.TTF
%{ttffontsdir}/COUNTERS.TTF
%{ttffontsdir}/CRACKMAN.TTF
%{ttffontsdir}/CREDITRI.TTF
%{ttffontsdir}/CREDITVA.TTF
%{ttffontsdir}/CREDITVB.TTF
%{ttffontsdir}/CREDITVI.TTF
%{ttffontsdir}/CREDITVZ.TTF
%{ttffontsdir}/CRETINO_.TTF
%{ttffontsdir}/CRYSTALR.TTF
%{ttffontsdir}/CUOMOTYP.TTF
%{ttffontsdir}/DEFTONE.TTF
%{ttffontsdir}/DEGRASSI.TTF
%{ttffontsdir}/DELTAHEY.TTF
%{ttffontsdir}/DELUXEDU.TTF
%{ttffontsdir}/DENDRITI.TTF
%{ttffontsdir}/DEPORTEE.TTF
%{ttffontsdir}/DIRTYDOZ.TTF
%{ttffontsdir}/DREAMOBX.TTF
%{ttffontsdir}/DREAMORB.TTF
%{ttffontsdir}/DREAMORI.TTF
%{ttffontsdir}/DREAMORP.TTF
%{ttffontsdir}/DUALITY_.TTF
%{ttffontsdir}/DYSPEPSI.TTF
%{ttffontsdir}/EARWIGFA.TTF
%{ttffontsdir}/EDENMB__.TTF
%{ttffontsdir}/EDENMI__.TTF
%{ttffontsdir}/EDENM___.TTF
%{ttffontsdir}/EDGEWATE.TTF
%{ttffontsdir}/ELECTBGI.TTF
%{ttffontsdir}/ELECTBGU.TTF
%{ttffontsdir}/ELECTBLU.TTF
%{ttffontsdir}/ELECTROH.TTF
%{ttffontsdir}/ENNOBLED.TTF
%{ttffontsdir}/EYERHYME.TTF
%{ttffontsdir}/FABIAN__.TTF
%{ttffontsdir}/FADGOD.TTF
%{ttffontsdir}/FAKERECE.TTF
%{ttffontsdir}/FIELDDAY.TTF
#%{ttffontsdir}/$FIVEDOU.TTF
%{ttffontsdir}/FLUORIDE.TTF
%{ttffontsdir}/FORGOTBI.TTF
%{ttffontsdir}/FORGOTTB.TTF
%{ttffontsdir}/FORGOTTE.TTF
%{ttffontsdir}/FORGOTTI.TTF
%{ttffontsdir}/FORGOTTR.TTF
%{ttffontsdir}/FORGOTTS.TTF
%{ttffontsdir}/FORGOTTY.TTF
%{ttffontsdir}/FRAGILEB.TTF
%{ttffontsdir}/FRAK.TTF
%{ttffontsdir}/FROZEN.TTF
%{ttffontsdir}/GIANTTIG.TTF
%{ttffontsdir}/GLAZKRAK.TTF
%{ttffontsdir}/GOLDENGI.TTF
%{ttffontsdir}/GOODFISB.TTF
%{ttffontsdir}/GOODFISC.TTF
%{ttffontsdir}/GOODFISH.TTF
%{ttffontsdir}/GOODFISI.TTF
%{ttffontsdir}/GOODTIME.TTF
%{ttffontsdir}/GOTNOHEA.TTF
%{ttffontsdir}/GRAFFITI.TTF
%{ttffontsdir}/GREENFUZ.TTF
%{ttffontsdir}/GROOVYGH.TTF
%{ttffontsdir}/GYPARODY.TTF
%{ttffontsdir}/GYRUSSIA.TTF
%{ttffontsdir}/HAMMAMAM.TTF
%{ttffontsdir}/HAWKEYE_.TTF
%{ttffontsdir}/HAWKEYE.TTF
%{ttffontsdir}/HEAVYHEA.TTF
%{ttffontsdir}/HELLOLAR.TTF
%{ttffontsdir}/HOLYSMOK.TTF
%{ttffontsdir}/HOMESWEE.TTF
%{ttffontsdir}/HOOKEDON.TTF
%{ttffontsdir}/HOOKED.TTF
%{ttffontsdir}/HORSPOWR.TTF
%{ttffontsdir}/HOTS.TTF
%{ttffontsdir}/HURONTAR.TTF
%{ttffontsdir}/HURRYUP.TTF
%{ttffontsdir}/HUSKYSTA.TTF
%{ttffontsdir}/HYDROGEN.TTF
%{ttffontsdir}/ICICLECO.TTF
%{ttffontsdir}/INDUCTIO.TTF
%{ttffontsdir}/INFLAMMA.TTF
%{ttffontsdir}/INSTANTT.TTF
%{ttffontsdir}/INTERPLA.TTF
%{ttffontsdir}/IOMANOID.TTF
%{ttffontsdir}/JIGSAWTR.TTF
%{ttffontsdir}/JINGOPOP.TTF
%{ttffontsdir}/JOHNNYFE.TTF
%{ttffontsdir}/KARMASUT.TTF
%{ttffontsdir}/KICKINGL.TTF
%{ttffontsdir}/KIMBERLE.TTF
%{ttffontsdir}/KINGRICH.TTF
%{ttffontsdir}/KINGRICI.TTF
%{ttffontsdir}/KREDIT1.TTF
%{ttffontsdir}/KUSTOMKA.TTF
%{ttffontsdir}/LARABIEB.TTF
%{ttffontsdir}/LARABIEF.TTF
#%{ttffontsdir}/LET'SEAT.TTF
%{ttffontsdir}/LETTERA.TTF
%{ttffontsdir}/LETTERB.TTF
%{ttffontsdir}/LETTERC.TTF
%{ttffontsdir}/LEWINSKY.TTF
%{ttffontsdir}/LIBEL.TTF
%{ttffontsdir}/LILLIPUT.TTF
%{ttffontsdir}/LIVINGBY.TTF
%{ttffontsdir}/LOCKERGN.TTF
%{ttffontsdir}/LUCKYAPE.TTF
%{ttffontsdir}/LUNASEQU.TTF
%{ttffontsdir}/LUNASOL.TTF
%{ttffontsdir}/LUNAUROR.TTF
%{ttffontsdir}/LUNECLPS.TTF
%{ttffontsdir}/MAITAI.TTF
%{ttffontsdir}/MALACHE.TTF
%{ttffontsdir}/MAPOFYOU.TTF
%{ttffontsdir}/MARQUEEM.TTF
%{ttffontsdir}/MASSIVER.TTF
%{ttffontsdir}/METALORD.TTF
%{ttffontsdir}/MEXCEL3D.TTF
%{ttffontsdir}/MEXCELLE.TTF
%{ttffontsdir}/MINYA.TTF
%{ttffontsdir}/MISIRLOD.TTF
%{ttffontsdir}/MISIRLOU.TTF
%{ttffontsdir}/MISSISSA.TTF
%{ttffontsdir}/MISTERFI.TTF
%{ttffontsdir}/MLURMLRY.TTF
%{ttffontsdir}/MOBCONCR.TTF
%{ttffontsdir}/MODELWOR.TTF
%{ttffontsdir}/MOLDPAPA.TTF
%{ttffontsdir}/MOTORCAD.TTF
%{ttffontsdir}/NASAL.TTF
%{ttffontsdir}/NEUROCHR.TTF
%{ttffontsdir}/NEUROPOL.TTF
%{ttffontsdir}/NEWBRILL.TTF
%{ttffontsdir}/NIGHTCOU.TTF
%{ttffontsdir}/NIGHTPOR.TTF
%{ttffontsdir}/OCTOVILL.TTF
%{ttffontsdir}/OPERATIO.TTF
%{ttffontsdir}/OUIJADOR.TTF
%{ttffontsdir}/OUTRIGHT.TTF
%{ttffontsdir}/OVERLOAD.TTF
%{ttffontsdir}/PAINTBOY.TTF
%{ttffontsdir}/PANTSPAT.TTF
%{ttffontsdir}/PARAAMIN.TTF
%{ttffontsdir}/PASTOROF.TTF
%{ttffontsdir}/PEATLOAF.TTF
%{ttffontsdir}/PLAINCRE.TTF
%{ttffontsdir}/PLANETBE.TTF
%{ttffontsdir}/PLASTICB.TTF
%{ttffontsdir}/POBEEF.TTF
%{ttffontsdir}/POKE.TTF
%{ttffontsdir}/POPUP.TTF
%{ttffontsdir}/PRIMEMIN.TTF
%{ttffontsdir}/PRIMERB.TTF
%{ttffontsdir}/PRIMER.TTF
%{ttffontsdir}/PULSESTA.TTF
%{ttffontsdir}/PYRITE.TTF
%{ttffontsdir}/QUADRANG.TTF
%{ttffontsdir}/QUANTITY.TTF
%{ttffontsdir}/QUININE.TTF
%{ttffontsdir}/QUINOLIN.TTF
%{ttffontsdir}/QUINQUEF.TTF
%{ttffontsdir}/QUIXOTIC.TTF
%{ttffontsdir}/RADIOHAR.TTF
%{ttffontsdir}/RADIOSIN.TTF
%{ttffontsdir}/RAZORKEE.TTF
%{ttffontsdir}/RELISHGA.TTF
%{ttffontsdir}/RIOTACT.TTF
%{ttffontsdir}/ROBOKOZ.TTF
%{ttffontsdir}/ROTHWELL.TTF
%{ttffontsdir}/RUSTPROO.TTF
%{ttffontsdir}/SADFILMS.TTF
%{ttffontsdir}/SANDOVAL.TTF
%{ttffontsdir}/SCREENGE.TTF
%{ttffontsdir}/SCRITZY.TTF
%{ttffontsdir}/SENDCASH.TTF
%{ttffontsdir}/SEXSMITH.TTF
%{ttffontsdir}/SHIFTY.TTF
%{ttffontsdir}/SHLOP___.TTF
%{ttffontsdir}/SHLOP.TTF
%{ttffontsdir}/SHOULDVE.TTF
%{ttffontsdir}/SHOULDVS.TTF
%{ttffontsdir}/SILICONC.TTF
%{ttffontsdir}/SKELETOR.TTF
%{ttffontsdir}/SLOEGIN.TTF
%{ttffontsdir}/Snidely.ttf
%{ttffontsdir}/SNIDELY_.TTF
%{ttffontsdir}/SOFACHRI.TTF
%{ttffontsdir}/SOFACHRO.TTF
%{ttffontsdir}/SORUNDOW.TTF
%{ttffontsdir}/SOULMAMA.TTF
%{ttffontsdir}/SOULPAPA.TTF
%{ttffontsdir}/SQUEALEM.TTF
%{ttffontsdir}/SQUEALER.TTF
%{ttffontsdir}/SRSERVIC.TTF
%{ttffontsdir}/STEREOFI.TTF
%{ttffontsdir}/STILLTIM.TTF
%{ttffontsdir}/STITCH.TTF
%{ttffontsdir}/STREETCR.TTF
%{ttffontsdir}/STUPEFAC.TTF
%{ttffontsdir}/STYROFOA.TTF
%{ttffontsdir}/SUDBURY3.TTF
%{ttffontsdir}/SUDBURY.TTF
%{ttffontsdir}/SUIGBI__.TTF
%{ttffontsdir}/SUIGB___.TTF
%{ttffontsdir}/SUIGENER.TTF
%{ttffontsdir}/SUIGI___.TTF
%{ttffontsdir}/SUPERGLU.TTF
%{ttffontsdir}/SUPERHET.TTF
%{ttffontsdir}/SWITCHIN.TTF
%{ttffontsdir}/TERYLENE.TTF
%{ttffontsdir}/THIAMINE.TTF
%{ttffontsdir}/TINSNIPS.TTF
%{ttffontsdir}/TOBINTAX.TTF
%{ttffontsdir}/TOFU.TTF
%{ttffontsdir}/TOMMYGUN.TTF
%{ttffontsdir}/TOPBOND.TTF
%{ttffontsdir}/TORKBI__.TTF
%{ttffontsdir}/TORKB___.TTF
%{ttffontsdir}/TORKI___.TTF
%{ttffontsdir}/TORK____.TTF
%{ttffontsdir}/TRAPPERJ.TTF
%{ttffontsdir}/TRIACSEV.TTF
%{ttffontsdir}/TROLLBAI.TTF
%{ttffontsdir}/UNIVOX.TTF
%{ttffontsdir}/UNSTEADY.TTF
%{ttffontsdir}/URKELIAN.TTF
%{ttffontsdir}/URURMA.TTF
%{ttffontsdir}/VADEMECU.TTF
%{ttffontsdir}/VANILLA.TTF
%{ttffontsdir}/VANISHIN.TTF
%{ttffontsdir}/VDUB.TTF
%{ttffontsdir}/VENUSRIS.TTF
%{ttffontsdir}/VIBROCEB.TTF
%{ttffontsdir}/VIBROCEI.TTF
%{ttffontsdir}/VIBROCEN.TTF
%{ttffontsdir}/VIBROCEX.TTF
%{ttffontsdir}/WAKEBAKE.TTF
%{ttffontsdir}/WALSHESO.TTF
%{ttffontsdir}/WALSHES.TTF
%{ttffontsdir}/WEBSTERW.TTF
%{ttffontsdir}/WELFAREB.TTF
%{ttffontsdir}/WETPET.TTF
%{ttffontsdir}/WHITELAK.TTF
%{ttffontsdir}/WILDSEWE.TTF
%{ttffontsdir}/WINTERMU.TTF
%{ttffontsdir}/WORLDOFW.TTF
%{ttffontsdir}/WORTHLES.TTF
%{ttffontsdir}/XENOWORT.TTF
%{ttffontsdir}/XOLTO.TTF
%{ttffontsdir}/XTRAFLEX.TTF
%{ttffontsdir}/!Y2KBUG.TTF
%{ttffontsdir}/YADOU.TTF
%{ttffontsdir}/YAWNOVIS.TTF
%{ttffontsdir}/YBANDTUN.TTF
%{ttffontsdir}/YELLOWPI.TTF
%{ttffontsdir}/YONDERRE.TTF
%{ttffontsdir}/YOUREGOI.TTF
%{ttffontsdir}/YOUREGON.TTF
%{ttffontsdir}/YYTRIUMD.TTF
%{ttffontsdir}/ZEKTONDO.TTF
%{ttffontsdir}/ZEROES__.TTF
%{ttffontsdir}/ZEROHOUR.TTF
%{ttffontsdir}/ZEROTHRE.TTF
%{ttffontsdir}/ZODILLIN.TTF
