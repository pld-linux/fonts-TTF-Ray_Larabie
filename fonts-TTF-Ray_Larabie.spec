Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Raya Larabie
Name:		fonts-TTF-Ray_Larabie
Version:	20030620
Release:	0.1
License:	Freeware
Group:		X11/Fonts
Source0:	http://www.larabiefonts.com/pig/allfonts.zip
# Source0-md5:	491a0e85c79e71b1d96a99a22e1fc1f9
URL:		http://www.larabiefonts.com/
#NoSource:	0
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Free TTF fonts created by Ray Larabie.

%description -l pl
Darmowe czcionki TTF napisane przez Raya Larabie.

%package -n %{name}-pl
Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Raya Larabie
Group:		X11/Fonts
Requires(post,postun):	fontpostinst
Requires(post,postun):	fontpostinst

%description -n %{name}-pl
A collection of free TrueType fonts. This package contains fonts with
iso8859-2 encoding.

%description -n %{name}-pl -l pl
Kolekcja darmowych czcionek TTF. W pakiecie tym znajduj± siê czcionki
zawieraj±ce kodowanie iso8859-2

%package -n %{name}-plbad
Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Raya Larabie
Group:		X11/Fonts
Requires(post,postun):	fontpostinst
Requires(post,postun):	fontpostinst

%description -n %{name}-plbad
A collection of free TrueType fonts. This package contains fonts with
iso8859-2 encoding, but Polish diacritical characters are not
displayed.

%description -n %{name}-plbad -l pl
Kolekcja darmowych czcionek TTF. W pakiecie tym znajduj± siê czcionki
zawieraj±ce kodowanie iso8859-2 ale polskie znaki nie s± wy¶wietlane.

%package -n %{name}-other
Summary:	Free TTF fonts created by Ray Larabie
Summary(pl):	Darmowe czcionki TTF napisane przez Raya Larabie
Group:		X11/Fonts
Requires(post,postun):	fontpostinst
Requires(post,postun):	fontpostinst

%description -n %{name}-other
A collection of free TrueType fonts. This package contains fonts with
enconding other than iso8859-2.

%description -n %{name}-other -l pl
Kolekcja darmowych czcionek TTF. W pakiecie tym znajduj± siê czcionki
nie zawieraj±ce kodowania iso8859-2.

%prep
%setup -q -c -T
unzip %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{ttffontsdir}

install *.TTF $RPM_BUILD_ROOT/%{ttffontsdir}
install *.ttf $RPM_BUILD_ROOT/%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{name}-pl
fontpostinst TTF

%postun -n %{name}-pl
fontpostinst TTF

%post -n %{name}-plbad
fontpostinst TTF

%postun -n %{name}-plbad
fontpostinst TTF

%post -n %{name}-other
fontpostinst TTF

%postun -n %{name}-other
fontpostinst TTF

%files -n %{name}-pl
%defattr(644,root,root,755)
%doc READ_ME.TXT TEEN.TXT
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
%{ttffontsdir}/ALMONTE.TTF
%{ttffontsdir}/ANGLEPOI.TTF
%{ttffontsdir}/AXAXAX.TTF
%{ttffontsdir}/BALTAR.TTF
%{ttffontsdir}/BORG9.TTF
%{ttffontsdir}/BUTTERBE.TTF
%{ttffontsdir}/CARBONBL.TTF
%{ttffontsdir}/CARBONPH.TTF
%{ttffontsdir}/CHARLESI.TTF
%{ttffontsdir}/CHINESER.TTF
%{ttffontsdir}/CONTOURG.TTF
%{ttffontsdir}/COOLVETI.TTF
%{ttffontsdir}/CRANBERR.TTF
%{ttffontsdir}/DIENASTY.TTF
%{ttffontsdir}/DIGNITY.TTF
%{ttffontsdir}/DROID___.TTF
%{ttffontsdir}/ECHECI__.TTF
%{ttffontsdir}/ECHEC___.TTF
%{ttffontsdir}/ECHEI___.TTF
%{ttffontsdir}/ECHELON_.TTF
%{ttffontsdir}/EFFLANTI.TTF
%{ttffontsdir}/EFFLBI__.TTF
%{ttffontsdir}/EFFLB___.TTF
%{ttffontsdir}/EFFLI___.TTF
%{ttffontsdir}/EFFLORES.TTF
%{ttffontsdir}/ETHNOCEN.TTF
%{ttffontsdir}/EUPHORIG.TTF
%{ttffontsdir}/FAILED.TTF
%{ttffontsdir}/GHOSTMEA.TTF
%{ttffontsdir}/HECK.TTF
%{ttffontsdir}/HEMIHEAD.TTF
%{ttffontsdir}/JOYSTIX.TTF
%{ttffontsdir}/KENYCBI_.TTF
%{ttffontsdir}/KENYCB__.TTF
%{ttffontsdir}/KENYCI__.TTF
%{ttffontsdir}/KENYC___.TTF
%{ttffontsdir}/KLEPTOCR.TTF
%{ttffontsdir}/LADYSTAR.TTF
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
%{ttffontsdir}/PLASMATI.TTF
%{ttffontsdir}/PRESGRG.TTF
%{ttffontsdir}/PRIMA___.TTF
%{ttffontsdir}/QUADAPTO.TTF
%{ttffontsdir}/SAVEDBYZ.TTF
%{ttffontsdir}/SPONGY.TTF
%{ttffontsdir}/SYBIG___.TTF
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
%doc READ_ME.TXT BETSY.TXT COUNTERS.TXT 
%{ttffontsdir}/1980PORT.TTF
%{ttffontsdir}/256BYTES.TTF
%{ttffontsdir}/6809CHAR.TTF
%{ttffontsdir}/ABBERANC.TTF
%{ttffontsdir}/ADRIATOR.TTF
%{ttffontsdir}/AIRMOLEA.TTF
%{ttffontsdir}/AIRMOLEQ.TTF
%{ttffontsdir}/AIRMOLES.TTF
%{ttffontsdir}/AIRMOLE.TTF
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
%{ttffontsdir}/BITINGOU.TTF
%{ttffontsdir}/BITING.TTF
%{ttffontsdir}/BORON2.TTF
%{ttffontsdir}/BUDMOB.TTF
%{ttffontsdir}/BUDMO.TTF
%{ttffontsdir}/BURNSTOW.TTF
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
%{ttffontsdir}/DENDRITI.TTF
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
%{ttffontsdir}/ELECTBGI.TTF
%{ttffontsdir}/ELECTBGU.TTF
%{ttffontsdir}/ELECTBLU.TTF
%{ttffontsdir}/ELECTROH.TTF
%{ttffontsdir}/ENNOBLED.TTF
%{ttffontsdir}/FABIAN__.TTF
%{ttffontsdir}/FADGOD.TTF
%{ttffontsdir}/FAKERECE.TTF
%{ttffontsdir}/FLUORIDE.TTF
%{ttffontsdir}/FORGOTBI.TTF
%{ttffontsdir}/FORGOTTB.TTF
%{ttffontsdir}/FORGOTTE.TTF
%{ttffontsdir}/FORGOTTI.TTF
%{ttffontsdir}/FORGOTTS.TTF
%{ttffontsdir}/FRAGILEB.TTF
%{ttffontsdir}/FROZEN.TTF
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
%{ttffontsdir}/HEAVYHEA.TTF
%{ttffontsdir}/HELLOLAR.TTF
%{ttffontsdir}/HOMESWEE.TTF
%{ttffontsdir}/HOTS.TTF
%{ttffontsdir}/HURRYUP.TTF
%{ttffontsdir}/HUSKYSTA.TTF
%{ttffontsdir}/HYDROGEN.TTF
%{ttffontsdir}/INFLAMMA.TTF
%{ttffontsdir}/INTERPLA.TTF
%{ttffontsdir}/IOMANOID.TTF
%{ttffontsdir}/KICKINGL.TTF
%{ttffontsdir}/KIMBERLE.TTF
%{ttffontsdir}/KINGRICH.TTF
%{ttffontsdir}/KINGRICI.TTF
%{ttffontsdir}/KREDIT1.TTF
%{ttffontsdir}/LARABIEB.TTF
%{ttffontsdir}/LARABIEF.TTF
%{ttffontsdir}/LETTERA.TTF
%{ttffontsdir}/LETTERB.TTF
%{ttffontsdir}/LETTERC.TTF
%{ttffontsdir}/LEWINSKY.TTF
%{ttffontsdir}/LILLIPUT.TTF
%{ttffontsdir}/LIVINGBY.TTF
%{ttffontsdir}/LOCKERGN.TTF
%{ttffontsdir}/LUCKYAPE.TTF
%{ttffontsdir}/LUNASOL.TTF
%{ttffontsdir}/MALACHE.TTF
%{ttffontsdir}/MAPOFYOU.TTF
%{ttffontsdir}/MARQUEEM.TTF
%{ttffontsdir}/METALORD.TTF
%{ttffontsdir}/MEXCEL3D.TTF
%{ttffontsdir}/MEXCELLE.TTF
%{ttffontsdir}/MISIRLOD.TTF
%{ttffontsdir}/MISIRLOU.TTF
%{ttffontsdir}/MOBCONCR.TTF
%{ttffontsdir}/MODELWOR.TTF
%{ttffontsdir}/MOTORCAD.TTF
%{ttffontsdir}/NEUROCHR.TTF
%{ttffontsdir}/NEUROPOL.TTF
%{ttffontsdir}/NEWBRILL.TTF
%{ttffontsdir}/PANTSPAT.TTF
%{ttffontsdir}/PLANETBE.TTF
%{ttffontsdir}/PLASTICB.TTF
%{ttffontsdir}/POBEEF.TTF
%{ttffontsdir}/POKE.TTF
%{ttffontsdir}/POPUP.TTF
%{ttffontsdir}/PRIMEMIN.TTF
%{ttffontsdir}/QUIXOTIC.TTF
%{ttffontsdir}/RADIOHAR.TTF
%{ttffontsdir}/RADIOSIN.TTF
%{ttffontsdir}/RAZORKEE.TTF
%{ttffontsdir}/RELISHGA.TTF
%{ttffontsdir}/RUSTPROO.TTF
%{ttffontsdir}/SANDOVAL.TTF
%{ttffontsdir}/SCREENGE.TTF
%{ttffontsdir}/SEXSMITH.TTF
%{ttffontsdir}/SHIFTY.TTF
%{ttffontsdir}/SHLOP___.TTF
%{ttffontsdir}/SHOULDVE.TTF
%{ttffontsdir}/SHOULDVS.TTF
%{ttffontsdir}/SKELETOR.TTF
%{ttffontsdir}/SLOEGIN.TTF
%{ttffontsdir}/SOFACHRI.TTF
%{ttffontsdir}/SOFACHRO.TTF
%{ttffontsdir}/SQUEALEM.TTF
%{ttffontsdir}/SQUEALER.TTF
%{ttffontsdir}/STEREOFI.TTF
%{ttffontsdir}/STILLTIM.TTF
%{ttffontsdir}/STREETCR.TTF
%{ttffontsdir}/STYROFOA.TTF
%{ttffontsdir}/SUDBURY3.TTF
%{ttffontsdir}/SUDBURY.TTF
%{ttffontsdir}/SUIGBI__.TTF
%{ttffontsdir}/SUIGB___.TTF
%{ttffontsdir}/SUIGENER.TTF
%{ttffontsdir}/SUIGI___.TTF
%{ttffontsdir}/SUPERGLU.TTF
%{ttffontsdir}/TERYLENE.TTF
%{ttffontsdir}/THIAMINE.TTF
%{ttffontsdir}/TINSNIPS.TTF
%{ttffontsdir}/TRAPPERJ.TTF
%{ttffontsdir}/TRIACSEV.TTF
%{ttffontsdir}/TROLLBAI.TTF
%{ttffontsdir}/UNIVOX.TTF
%{ttffontsdir}/UNSTEADY.TTF
%{ttffontsdir}/URKELIAN.TTF
%{ttffontsdir}/VADEMECU.TTF
%{ttffontsdir}/VANILLA.TTF
%{ttffontsdir}/VDUB.TTF
%{ttffontsdir}/VENUSRIS.TTF
%{ttffontsdir}/VIBROCEB.TTF
%{ttffontsdir}/VIBROCEI.TTF
%{ttffontsdir}/VIBROCEN.TTF
%{ttffontsdir}/VIBROCEX.TTF
%{ttffontsdir}/WAKEBAKE.TTF
%{ttffontsdir}/WALSHES.TTF
%{ttffontsdir}/WELFAREB.TTF
%{ttffontsdir}/WILDSEWE.TTF
%{ttffontsdir}/WINTERMU.TTF
%{ttffontsdir}/WORLDOFW.TTF
%{ttffontsdir}/XOLTO.TTF
%{ttffontsdir}/!Y2KBUG.TTF
%{ttffontsdir}/YONDERRE.TTF
%{ttffontsdir}/YOUREGOI.TTF
%{ttffontsdir}/YOUREGON.TTF
%{ttffontsdir}/YYTRIUMD.TTF
%{ttffontsdir}/ZEKTONDO.TTF
%{ttffontsdir}/ZEROES__.TTF
%{ttffontsdir}/ZEROTHRE.TTF
%{ttffontsdir}/ZODILLIN.TTF

#to check
%{ttffontsdir}/BLUEHIGD.TTF
%{ttffontsdir}/FOO.TTF
%{ttffontsdir}/HEARTSWE.TTF
%{ttffontsdir}/HOMESWEO.TTF
%{ttffontsdir}/JUNEGULL.TTF
%{ttffontsdir}/KIMBALT_.TTF
%{ttffontsdir}/LET'SEAT.TTF
%{ttffontsdir}/NUMBERPI.TTF
%{ttffontsdir}/OCTOVILL.TTF
%{ttffontsdir}/OILCRISA.TTF
%{ttffontsdir}/OILCRISB.TTF
%{ttffontsdir}/PRIMER.ttf
%{ttffontsdir}/PRIMERB.ttf
%{ttffontsdir}/RAFIKA__.TTF
%{ttffontsdir}/SAPPM___.TTF
%{ttffontsdir}/STEELOUT.TTF
%{ttffontsdir}/STRENU3D.TTF
%{ttffontsdir}/TORKBI__.TTF
%{ttffontsdir}/TORKB___.ttf
%{ttffontsdir}/TORKI___.ttf
%{ttffontsdir}/TORK____.ttf
%{ttffontsdir}/VELVENDC.TTF
%{ttffontsdir}/VINQUE.TTF
%{ttffontsdir}/ZEROHOUR.ttf
%{ttffontsdir}/ZORQUE.TTF
