# Konkrete Prüfung der vorhandenen Kernel und Linux-Module

[Übersicht](../README.md) · [Lizenzanforderungen](distribution.md) · [Hardwarestatus](status.md)

## Ergebnis

**Für das abgegrenzte experimentelle Grafik-/USB4-Release liegt ein vollständig zusammengestellter und unabhängig geprüfter lokaler Quellen-/Binärkandidat vor.** Vollständige Quellen, tatsächliche Buildsteuerung und Konfiguration, erforderliche Lizenzvolltexte, korrigierter GPU-Helfer und die belegten lokalen Änderungshinweise sind paketiert. Die früheren Lücken bei FF-A und PCI sind damit für diesen Kandidaten geschlossen. Das ist keine pauschale Rechtsgarantie, keine Freigabe alter Arbeitsarchive und insbesondere keine Abnahme einer sicheren nativen Installation. Der Public-v1-Kernel wurde noch nicht auf dem Yoga gebootet; Audio und Kamera werden nicht als funktionierend angeboten. Commit, Upload und Veröffentlichung sind nicht erfolgt.

Die ursprünglichen Audits erfolgten offline an gespeicherten Artefakten; der spätere separate Neubau ist in Abschnitt 3 beschrieben. Die Yoga-Installation blieb unverändert. Linux-Lizenzen, öffentliche Nachbaubarkeit, Datenschutz und tatsächliche Hardwarefunktion sind getrennte Kriterien.

## 1. Die zwei tatsächlich gebauten Kernel

Der Name `7.2.8-yoga-nvidia` bezeichnet im akzeptierten Rückfallpfad einen **Booteintrag**, keinen eigenständig unter diesem Namen kompilierten Kernel. Er verwendet das Image mit dem tatsächlichen Kernelrelease **`7.2.8-yoga-usb4-v2`**. Das ist insbesondere für die Zuordnung externer Module wichtig.

| Artefakt | Tatsächliches Kernelrelease | SHA256 des untersuchten Image |
|---|---|---|
| Akzeptierter Grafik-/USB4-Rückfallpfad | `7.2.8-yoga-usb4-v2` | `b4de18b840f7ce542e7c803ce44b2a83653bca1ca4ad83ca38c5f37432f5209a` |
| Audio-Diagnosekernel | `7.2.8-yoga-audio-v2` | `1611a750921cfc5f0ee7b6b673f00c553d3566b83cfe49a90c9c8b21daaf32dd` |

Bei beiden Images stimmt die direkt aus dem Binärimage extrahierte Konfiguration bytegenau mit der gespeicherten finalen Buildkonfiguration überein. Die erneute Umwandlung des gespeicherten `vmlinux` mit den protokollierten `objcopy`-Optionen ergab jeweils wieder die exakten Imagebytes. Das verknüpft Image, ELF und Konfiguration, beweist aber noch nicht sämtliche historischen Compiler-Eingaben oder einen reproduzierbaren Neubau.

### Quellen und Patchfolge

Die gespeicherte Basis ist Linux `7.2.8`; die zusätzlichen Plattformquellen stammen unter anderem aus dem festgehaltenen Omarchy-Quellstand `4114f7fa2b7a7548cdee93421ba435f8a7df9b8b`:

- [Linux-Quellarchiv](https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-7.2.8.tar.xz)
- [Festgehaltener Plattform-Paketstand](https://github.com/omacom/omarchy-pkgs/tree/4114f7fa2b7a7548cdee93421ba435f8a7df9b8b/pkgbuilds/linux-omarchy-aarch64)

**Die heruntergeladenen Patches einfach numerisch anzuwenden, reproduziert diese Kernel nicht.** Bei der Kontrollanwendung wurden Hunks aus vier Patches abgewiesen; einzelne Änderungen wurden lokal angepasst oder nicht übernommen. Eine solche pauschale Patchliste wäre deshalb keine korrekte öffentliche Bauanleitung.

Stattdessen wurden exakte Gesamtdifferenzen gegenüber dem gespeicherten Linux-Archiv und sieben lokale Entwicklungsstufen ermittelt. Daraus wurden inzwischen zwei vollständige **interne Quellarchiv-Entwürfe** einschließlich exakter finaler Konfiguration, Original-Lizenzdateien, Inventaren und dokumentierter Buildaufrufe erstellt. Die unabhängige Prüfung direkt aus den erzeugten Archiven bestätigte alle 94.793 regulären Dateien des Rückfall-Quellbaums beziehungsweise 94.816 des Audio-Quellbaums sowie jeweils 99 Symlinks; keine fehlenden oder unerwarteten Quelleinträge, beide Konfigurationen identisch. Das ist eine vollständige Quellrekonstruktion, noch kein erfolgreicher Neubau oder öffentlich freigegebener Download.

| Interner Quellarchiv-Entwurf | SHA256 |
|---|---|
| `7.2.8-yoga-usb4-v2-source-DRAFT.tar.gz` | `2fdaae7b24aee4b4ab9feb70cfd5afde757a65d2f66d3f53ab191b58eceb1ed1` |
| `7.2.8-yoga-audio-v2-source-DRAFT.tar.gz` | `464915b013c95040841be1ef267c9f9375b93c8cbfbe0ce9885b972ac4341d92` |

Die zugehörigen externen Quellen liegen inzwischen separat als interner Entwurf `yoga-external-module-source-DRAFT.tar.gz` vor (SHA256 `0411286941c380400a224ed582eff7ccd37f207a400e28751eb695f1311ca17a`). Die unabhängige Prüfung bestätigte alle 47 äußeren Dateien und sämtliche 4.002 Dateien des enthaltenen NVIDIA-Originalquellarchivs. Enthalten sind außerdem die 25 exakten Audio-Quelleingänge, sechs ergänzende Schnittstellenheader, GPU-Helferquellen, Konfigurationen, Lizenzen und eine noch nicht ausgeführte Buildanleitung. Die abschließende Prüfung der kombinierten Corresponding Source einschließlich Rechte-/Hinweiseprüfung und Datenschutzfreigabe bleibt offen; der inzwischen tatsächlich ausgeführte bereinigte Grafik-/USB4-Neubau ist in Abschnitt 3 beschrieben. Unveränderte öffentliche Testschlüssel aus dem Linux-Basisarchiv sind Quelltestdaten, keine privaten Projekt- oder Buildschlüssel; ihre Identität zur gespeicherten Basis wurde separat bestätigt. Sie werden nicht mit privaten Schlüsseln gleichgesetzt oder zur pauschalen Sperre der Kernelquellen erklärt.

Gespeicherte Prüfsummen bestätigen die Identität der lokalen Eingänge. Die vorliegende Offline-Prüfung ist keine nachträgliche OpenPGP-Authentifizierung des ursprünglichen Downloads.

### Konkretes Metadatenhindernis

Beide Image-/ELF-Paare enthalten Build-Benutzer, Build-Host und zahlreiche absolute Buildwurzelpfade. Bei der untersuchten Pfadregex wurden pro Artefakt 1.845 Treffer gezählt, obwohl keine DWARF-Debuginformation enthalten ist. **Debugsymbole abzuschalten allein genügt daher nicht.** Die tatsächlichen Identitätswerte werden hier nicht veröffentlicht.

Außerdem enthält jedes untersuchte Kernelimage ein generiertes DER-Zertifikat. Ein öffentliches Zertifikat ist nicht mit einem privaten Schlüssel gleichzusetzen; Inhalt, Zweck und spätere Vertrauenskette müssen dennoch vor einer Veröffentlichung bewertet werden. Private Signierschlüssel und vollständige Build-Ausgabeverzeichnisse sind immer ausgeschlossen.

Für einen bereinigten Releasebau müssen Buildidentität, Quell-/Buildpfadbehandlung, Zeitstempel und Signierkonzept explizit festgelegt werden. Das verlangt einen separaten Build und neue Prüfungen, nicht nachträgliches Umschreiben akzeptierter Binärdateien. Ein solcher neuer Build übernimmt die bisherige Hardwareabnahme nicht automatisch.

## 2. Zwölf konkret untersuchte Linux-Module

| Gruppe | Tatsächlich untersuchte Dateien | Lizenzbefund | Noch nötige Releaseprüfung |
|---|---|---|---|
| Originale NVIDIA Open GPU Kernel Modules `615.78.08` | `nvidia.ko`, `nvidia-modeset.ko`, `nvidia-drm.ko`, `nvidia-uvm.ko` | Modulmetadaten `Dual MIT/GPL`; originale `COPYING` und Dateiausnahmen geprüft | Vollständige zugehörige Quellen, Buildskripte und Drittvermerke; Herkunft/Lizenz generierter und eingebetteter Daten; Buildpfade bereinigen |
| Residenter GPU-Metadatenhelfer | `yoga_gpu_gap.ko` | Quelle mit `GPL-2.0`, Modulmetadaten `GPL` | Quelle, datierte Änderungen und exakte Buildvoraussetzungen mitliefern; Laufzeit-Releaseguard korrigieren |
| Sieben No-stream-Module | `cs42l43-sdw.ko`, `cs42l43.ko`, `mt8901-acp-sdw-legacy-mach.ko`, `snd-soc-cs42l43-sdw.ko`, `snd-soc-cs42l43.ko`, `snd-soc-mt8901-afe.ko`, `soundwire-mtk.ko` | Quellen mit GPL-Vermerken; Modulmetadaten `GPL`; ursprüngliche Cirrus-/MediaTek-Vermerke vorhanden | Vollständige zugehörige Quellen und Schnittstellen, Buildskripte, Konfiguration, nachvollziehbare Änderungsvermerke und Berechtigung für neue Integration |

Die vier NVIDIA-Modulhashes stimmen mit dem gespeicherten Originalbuild überein; experimentelle Trace-/Fixvarianten sind nicht Gegenstand dieser Freigabespur. Die sieben No-stream-Modulhashes stimmen mit dem akzeptierten Parser-v1-Payload überein. Dessen 25 untersuchte Quelleingänge stimmen ebenfalls mit ihrem Manifest überein. Die anschließende unabhängige Kontrolle bestätigte alle 89 Einträge des gesamten ursprünglichen Payloadmanifests.

Die Vendor-Quellbäume stimmen mit allen 4.002 regulären Dateien des gespeicherten NVIDIA-Quellarchivs überein. Das ist mehr als eine Versionszeichenfolge, aber noch kein bitidentisch reproduzierter Modulbuild. Namen von generierten OS-unabhängigen Objektdateien beweisen für sich genommen keine proprietäre Lizenzierung; die passenden Quellen und Buildregeln sind vorhanden.

### Eingebettete Daten nicht übersehen

Im Modeset-Modul wurden fünf komprimierte Shaderblobs bytegenau zu den gespeicherten Vendor-Dateien zugeordnet. Deren bevorzugte Bearbeitungsform, Erzeugungsweg und geltende Hinweise sind noch konkret zuzuordnen. Auch in C-Arrays codierte Firmware kann Bestandteil eines Moduls sein; das Fehlen einer ausdrücklich so benannten ELF-Sektion ist kein Gegenbeweis.

Der NVIDIA-Kern enthält außerdem eingebettete Zertifikatsdaten. Diese sind von einer Modulsignatur zu unterscheiden. Bei den zwölf untersuchten Modulen wurden keine Modulsignierer oder Signaturtrailer festgestellt. Mehrere Module enthalten jedoch absolute Buildwurzelpfade. Negativbefunde bei Homepfaden und DWARF sind keine vollständige Datenschutzfreigabe.

**Nicht Teil dieser Lizenzfreigabespur:** NVIDIA-Userspace, extern geladene GPU-Firmware sowie aus Windows-Paketen extrahierte Treiber, Firmware und Lautsprechertuning. Diese Inhalte werden nicht automatisch durch die Lizenz offener Kernelmodule mitfreigegeben.

## 3. Tatsächlich ausgeführter bereinigter Neubau

Ein separater Grafik-/USB4-Kandidat **`7.2.8-yoga-usb4-public-v1`** ist inzwischen vollständig gebaut und intern paketiert. Er verändert weder die akzeptierten Originaldateien noch die Yoga-Installation. Seine Quellen entsprechen dem rekonstruierten Rückfall-Quellbaum; die neue finale Konfiguration liegt dem Binärpaket bei. Geändert wurden `CONFIG_LOCALVERSION` und der geleerte `CONFIG_BUILD_SALT`; `olddefconfig` ergänzte außerdem die zuvor nicht gespeicherte Compilerfähigkeit `CONFIG_CC_CAN_LINK=y`. Die übrigen vorhandenen Konfigurationsauswahlen blieben unverändert.

| Neuer interner Binärentwurf | SHA256 |
|---|---|
| `7.2.8-yoga-usb4-public-v1-kernel-INTERNAL-DRAFT.tar.gz` | `55beec2a9cdbee0c9afbae0bec7b49840c7c979ca3260914cfa871b7aa57b4eb` |
| `7.2.8-yoga-usb4-public-v1-graphics-INTERNAL-DRAFT.tar.gz` | `8ae33b7eab0c749084f0ca1b9b1fca655640b57a95001bf1d35db6aa9e5b34c9` |

Das neue Image hat SHA256 `6f32af5bbb4cda1b1dc0b9caab1b5708ace8095b989dd384ce5266af84198887`. Unabhängig aus den tatsächlichen Archiven geprüft wurden alle 173 regulären Mitglieder des Kernelpakets und alle 17 des Grafikpakets einschließlich ihrer internen Prüfsummen. Enthalten sind 145 In-tree-Module sowie vier neu gegen diesen Kernel gebaute originale NVIDIA-Module `615.78.08` und der GPU-Helfer. **Alle 150 Module sind AArch64 und haben dieselbe vollständige vermagic.** Die unabhängige kombinierte Prüfung mit `depmod -e -F System.map` endete ohne Warnungen. Sie bestätigt statische Abhängigkeiten, nicht die Lauffähigkeit auf der Hardware.

Die Buildprüfung fand keine bisherigen privaten Benutzer-/Host-/Buildwurzelwerte; der unabhängige begrenzte Nachscan der archivierten Binärdaten fand keine Home-/Rootpfade oder privaten Schlüsselmarker. Öffentliche Buildidentität und fester Zeitstempel sind im tatsächlichen Image nachgewiesen. Generische Containerpfade sind dennoch teilweise eingebettet; sie sind nicht persönlich und werden nicht als vollständig entfernt dargestellt. Der neu erzeugte private Signierschlüssel sowie rohe Logs und `vmlinux` sind nicht in den Archiven enthalten.

**Konkreter technischer Fehler trotz bestandener statischer ABI-Prüfung:** Quelle und ausgeliefertes `yoga_gpu_gap.ko` verlangen zur Laufzeit noch exakt `7.2.8-yoga-usb4-v2`. Der neue Kernel heißt `7.2.8-yoga-usb4-public-v1`; der Helfer verweigert deshalb dort seine Initialisierung. Der bisherige Grafikentwurf ist somit keine funktionsbereite Gesamtlösung. Eine separate Korrektur wurde inzwischen tatsächlich gebaut: Nur der exakte Release-Guard wurde auf das neue Release geändert, alle übrigen Quelltextbytes und Schutzprüfungen blieben erhalten. Der kompilierte C-Guard bestand 13 Prüfungen; im kombinierten Satz wurden genau der Helfer ersetzt und 149 Module bytegleich übernommen. Die erneute statische ABI-/depmod-Prüfung bestand. Das beweist keine Hardwarefunktion. Der korrigierte Helfer hat SHA256 `ef8991a07b7ae0126e973acf5d8a9d28d8e68f78e3a51558539989b110a244c9`; die separaten Archive `correction-source-v1.tar.gz` und `correction-binary-v1.tar.gz` haben SHA256 `af51a24716ce2cd821c4c04daf49e9c5ce30b9164a7785729aa2d86e879a0e4e` beziehungsweise `cd0394359fad88507b366bef95e8e8c0721d0bb9e966a420f712b90c45247941`. Der ursprüngliche fehlerhafte Entwurf bleibt unverändert und wird durch die Korrektur nicht rückwirkend freigegeben.

Die abschließende Quellenprüfung hat die tatsächlich ausgeführten Buildskripte, exakte Konfiguration und Metadaten als Quellergänzung paketiert. Deren Archiv `public-release-review-and-source-supplement-v1.tar.gz` hat SHA256 `b0fe832f6fce7d95b96666f63a9a458b579715eb2eb2b4c5a582ea11962b5c5b`. Das beigefügte Replay-Rezept wurde zusammengestellt, nicht als erneuter vollständiger Build ausgeführt.

**Lizenzvolltexte separat ergänzt:** Die zuvor fehlenden vollständigen DMTF/libspdm-BSD- und Apache-2.0-plus-LLVM-Ausnahmetexte liegen inzwischen mit Originalattributionen, Abrufbelegen und konkreter Dateizuordnung in `public-safe-license-supplement-v1.tar.gz` vor (SHA256 `b1d9d1e7a5cffca07b69266d3b147b8462df00e708bcdd7c854107952c474b40`). Dieses Supplement muss zusammen mit den betreffenden Quellen/Binärdateien mitgeliefert werden; die ursprünglichen Archive wurden nicht geändert. Die Verwendung des Clang-Headers im GCC-Binärbuild wurde nicht festgestellt. **Weiter offen:** Nachgewiesene lokale GPL-Dateiänderungen benötigen wahre prominente Änderungs-/Datumshinweise. Fehlende historische Daten werden nicht durch den festen Kbuild-Zeitstempel ersetzt. Die MIT-Defaultlizenz und ausdrücklichen NVIDIA-Dateiausnahmen bleiben erhalten; allein aus generierten Shaderdaten wird kein pauschaler GPL- oder Rechteblocker abgeleitet.

**Noch kein öffentlicher Download und keine Hardwareabnahme:** Dieser Kandidat wurde weder installiert noch gebootet. Installations-/Rückfallanleitung und tatsächlicher Einsatztest sind von Lizenz- und Quellvollständigkeit getrennte Aufgaben. Ein ehrlich gekennzeichnetes ungebootetes Experiment ist nicht allein wegen des fehlenden Hardwaretests rechtlich unverteilbar. Der neue Kernel ist keine fertige Audio-/Kameralösung.

## 4. Zusammengestellter Releasekandidat und Installationsgrenzen

Ein vollständiger lokaler Grafik-/USB4-Releasekandidat ist zusammengestellt: sieben Archive, README, Maschinenmanifest und Prüfsummenliste. Das Kernelarchiv ist bytegleich zum geprüften Neubau; das neue Grafikarchiv enthält bereits den korrigierten Helfer. Ein separates Korrekturoverlay ist dafür nicht nötig.

| Neues Kandidatenarchiv | SHA256 |
|---|---|
| `7.2.8-yoga-usb4-public-v1-graphics-corrected-v1.tar.gz` | `b702d2d015c391bfd9e39707912e0bee7b93a67958e76075cebd9bfcbe427225` |
| `yoga-graphics-external-source-v1.tar.gz` | `cf5d8c376e769bd7e91d3d152f2292ee011c7be009d5c641eccf4b8c4267c7f2` |
| `release-source-map-v1.tar.gz` | `169157413c5d29f65bf8af46370345a22e24516000a11f494569ca5a92cec8ff` |

Das fokussierte externe Quellpaket enthält alle 4.002 Vendor-Dateien, den korrigierten Helfer, tatsächliche Buildsteuerung und Lizenzergänzungen; unbenutzte externe Audioquellen bleiben getrennt. Vollständiges Kernelquellarchiv, exakte öffentliche Konfiguration und Buildkontrollen liegen im selben Kandidatensatz. Unabhängig bestätigt wurden alle neun äußeren Prüfsummeneinträge und der vollständige Satz von 150 Modulen direkt aus den beiden Binärarchiven, einschließlich AArch64, voller vermagic. **Der historische Tag der konkreten lokalen FF-A-Anpassung ist inzwischen belegt: 06.11.2026.** Die ursprünglichen erfolgreichen Änderungsaufrufe für SGI-Abbildung und `irqdomain.h` wurden erneut eingesehen; ihre Rekonstruktion entspricht der ausgelieferten Datei. Das ist kein pauschales erstes/letztes Änderungsdatum der gesamten Datei.

### Vollständige Kernelquelle mit eingebautem FF-A-Hinweis

Ein neuer separater Kandidat enthält den prominenten FF-A-Dateihinweis tatsächlich im vollständigen Quellarchiv, nicht nur als lose Ergänzung:

| Neues Archiv | SHA256 |
|---|---|
| `7.2.8-yoga-usb4-noticed-source-v1.tar.gz` | `cffe7a2ee94dd4ceeeb4843db5ebbe59ba3c6ba1b4b730a8beed98b0e99493c1` |
| `source-map-noticed-v1.tar.gz` | `12787dbb635e4af70866e7df0665b1c09b7213a4c50ce14e46663d9be6a2e5f0` |

Unabhängig vollständig verglichen wurden **94.793 reguläre Quelldateien und 99 Symlinks**. Nur `drivers/firmware/arm_ffa/driver.c` unterscheidet sich durch den Hinweis-Kommentar; alle übrigen Quelldateibytes und Symlinkziele sind unverändert. Das neue Archiv enthält insgesamt 101.108 Mitglieder einschließlich Verzeichnissen und Paketmetadaten. Der Hinweis nennt den belegten Anpassungstag und getrennt den Annotationstag 10.11.2026. Vorwärts-/Rückwärtspatches, unveränderte ursprüngliche Buildzuordnung und kommentarbefreiter gleicher Token-/Direktiveninhalt sind dokumentiert. **Kein Kernelneubau:** Der tatsächlich kompilierte Quellstand lässt sich durch Entfernen der Annotation exakt wiederherstellen; das neue kommentierte Archiv wird nicht als erneut gebaut ausgegeben.

Dieser Zwischenstand umfasst sieben Archive sowie README, Manifest und Prüfsummen. Alle neun äußeren Prüfsummeneinträge und die vollständige Lesbarkeit aller sieben Archive wurden unabhängig bestätigt. Kernel- und korrigiertes Grafikbinärarchiv bleiben bytegleich. Die bisherigen Kandidaten wurden nicht umgeschrieben. Der nachstehende Kandidat mit beiden Änderungshinweisen ersetzt ihn als aktuellen Vorbereitungsstand.

**Herkunfts-/Hinweisaudit der Stufen 01/02 abgeschlossen:** Alle 56 Rückfall-Delta-Pfade wurden durch tatsächlichen Patch-Replay klassifiziert: 50 unveränderte Drittanbieter-Patchübernahmen, vier erzeugte `.orig`-Sicherungen, ein normalisierter Upstream-Symlink ohne Implementierungsänderung und eine lokale Anpassung in `drivers/thunderbolt/pci.c`. Die unveränderten übernommenen Implementierungen benötigen keine erfundenen eigenen Bearbeitungsdaten; fremde Attributionen und Patchprovenienz bleiben erhalten. Die lokale Anpassung des abgewiesenen PCI-Teils von Patch 1075 an Vanilla Linux 7.2.8 ist durch den ursprünglichen erfolgreichen Änderungsvorgang vom **6. November 2026** belegt. Der prominente Kommentar nennt diesen Tag getrennt vom Annotationsdatum 10. November 2026 und ist inzwischen im nachstehenden vollständigen Quellpaket enthalten. Die bereits paketierte FF-A-Annotation bleibt erhalten.

### Aktueller vollständiger Kandidat mit beiden Änderungshinweisen

| Archiv | SHA256 |
|---|---|
| `7.2.8-yoga-usb4-complete-notices-source-v1.tar.gz` | `43b90acd44b8cdb650c1dd1736e260aa4996d5f4bb276dd4c7f8065598e709b1` |
| `source-map-complete-notices-v1.tar.gz` | `8e245386c4ce10ff6ec132f90a633dfdec81d871aabd6a297829839bbc3f5fec` |

Diese beiden Archive ersetzen die Quelle und Source-map des vorherigen Zwischenstands. Die fünf übrigen Begleitarchive sind bytegleich erhalten; alle sieben gehören zusammen. Der Kandidat enthält weiterhin **145 In-tree- und fünf Grafikmodule**, nicht automatisch den separat gebauten PFN-Prüfer oder Python-Controller. Das vollständige Quellarchiv enthält 94.793 reguläre Linuxdateien, sieben Paketdateien, 99 Symlinks und 6.209 Verzeichnisse: insgesamt 101.108 Member.

Die unabhängige Parentprüfung hat alle sieben Archive vollständig erneut gelesen, ihre äußeren Prüfsummen geprüft und die gesamte Quelle direkt mit dem vorherigen kommentierten sowie dem ursprünglich gebauten Quellarchiv verglichen. Gegenüber dem Zwischenstand unterscheidet sich nur der PCI-Kommentar; gegenüber der ursprünglichen Buildquelle nur PCI- und FF-A-Kommentar. Alle übrigen Quellbytes, Dateimodi und Linkziele sind identisch. Sämtliche 43 internen Source-map-Prüfsummen und die strukturierte 56-Pfad-Klassifizierung wurden ebenfalls geprüft.

Die Source-map enthält beide Kommentarpatches und `remove-all-publication-notices.patch`. Dessen tatsächliche Anwendung in einer unabhängigen Testkopie mit null Fuzz stellte die beiden ursprünglichen Builddateien bytegenau wieder her. GCC-Kommentarentfernung mit erhaltenen Direktiven ergab für beide Dateien identische Ergebnisse. **Kein Kernelneubau wurde daraus abgeleitet oder behauptet:** Die neuen Annotationen dokumentieren die vorhandenen Binärdateien; die exakte zuvor gebaute Quelle bleibt reproduzierbar rekonstruierbar. Der Satz ist lokal vorbereitet, nicht hochgeladen oder veröffentlicht.

### Separat gebauter unabhängiger PFN-Prüfer

`nv_pfn_probe.ko` wurde inzwischen ohne C-/Makefile-Änderung passend zum Public-v1-Kernel neu gebaut. Die ursprüngliche Quelle ist bytegleich zum erhaltenen Vollbereichsprüfer. Das neue Modul hat SHA256 `fd28ab4a9025b5c950df8c014e7c311dda890be06c3a07740bbd76b9043d92fd`. Zugehörige separate Archive:

| Archiv | SHA256 |
|---|---|
| `pfn-probe-source-v1.tar.gz` | `c9d0ea94ab9be8f0a9a04e0c78ac51d9a7a1fddd75f9c1008b5c1a302864f6d3` |
| `pfn-probe-binary-v1.tar.gz` | `346d1f78bdb26012df90140dfbd4f197914b809a2bca42bf47a4f5a147a8b865` |

Die unabhängige Wiederholung aus dem tatsächlichen Quellarchiv bestand fünf ausführbare C-Prüffälle. Jeder Fall besuchte sämtliche **16.888.320 PFNs** der drei Bereiche in Reihenfolge, einschließlich absichtlicher innerer Lücken und vollständig ungültiger Bereiche. Das verwendet simulierte Kernel-API-Grenzen, nicht echte Hardware. Alle bisherigen 150 Module blieben bytegleich; der separate kombinierte Satz mit 151 Modulen bestand AArch64-/vermagic-Prüfung und `depmod -e -F System.map` ohne Warnungen.

**Wichtiger Laufzeitvertrag:** Der unveränderte Prüfer liefert auch bei ungültigen PFNs Init-Erfolg. Exitcode 0 oder bloße Modulpräsenz sind daher keine Freigabe. Der Startcontroller muss die vollständigen frischen Bereichsergebnisse und den determinierten Abschluss prüfen; unklarer Abschluss erlaubt weder erneuten Versuch noch Unload/Reset. Der Reparaturhelfer bleibt resident. Der Prüfer besitzt keinen eigenen Modell-Guard; der vorgeschaltete exakte Release-/Modell-/Ressourcenvertrag ist unverzichtbar. Der neue Prüfer ist noch nicht in den oben beschriebenen sieben Kandidatenarchiven enthalten.

**Verbleibende Installationslücke:** Ein öffentlicher releasegebundener GPU-Startcontroller samt qualifizierter Autoload-/Initramfs-Policy ist noch nicht Bestandteil des Pakets. Der weiterentwickelte Controller bestand unabhängig wiederholt **31 Offline-Tests** einschließlich frischer vollständiger PFN-Auswertung, Stufenabbruch bei unbekannten Resultaten und Verweigerung bei Zustandswechseln. Der neue Probehash und dessen tatsächlicher Vertrag sind eingetragen. CLI und deaktivierte Reviewtemplates liegen vor; die CLI verweigert die native Ausführung mit Exitcode 2 **vor dem ersten Seiteneffekt**. Das ist eine getestete sichere Sperre, keine vollständige native Startintegration.

Noch fehlen effektive Firmware-/Userspace-/Autoload-/Initramfs-Verträge und deren vollständige native Verifizierer, vertrauenswürdige Datei-/Tool-/ELF-Prüfung, ein angebundener begrenzter echter Prozessrunner sowie SELinux-Validierung.

Der separate Prozesstransport liegt inzwischen als isoliertes Review-Artefakt vor; **18 Tests wurden unabhängig erneut bestanden**, einschließlich echter harmloser Kindprozesse für Timeout, Ausgabe-Flood, nicht erfolgreiche Exits, ungültiges UTF-8 und von Nachfahren offen gehaltene Pipes. Er liest beide Streams inkrementell mit gemeinsamem Bytebudget, verwendet eine monotone Deadline und wartet nach Transportabbruch nur begrenzt auf den direkten Kindprozess. Fehlermeldungen geben keine Rohargumente oder Prozessausgaben aus. Keine Shell-/PATH-Ausweichsuche, keine Umgebungsvererbung und keine automatischen Wiederholungen. Prozessgruppenbereinigung ist ausdrücklich kein Treiber-Rollback und kein Nachweis beendeter Kernel-I/O; ein nicht bestätigtes Prozessende sperrt weitere Starts. Werkzeugvertrauen und Austauschrennen prüft dieser Transport nicht. Die produktive Einbindung bleibt gesperrt: Transportfehler müssen als unbekannter Hardwarezustand ohne Entladen, Reset oder Wiederholung behandelt werden. Die vorliegenden Tests qualifizieren weder native Modulzugriffe noch Hardwarefunktion. Passende NVIDIA-Userspace-/Firmwareintegration und Secure-Boot-Vertrauen werden nicht durch den statischen Modulbuild nachgewiesen. Das sind getrennte Integrations-/Rechtefragen, kein pauschales Weiterverteilungsverbot der bereits lizenzierten Kernelquellen.

**Historischer erster Offline-Integrationsstand, native Sperre erhalten:** Ein neuer, nicht paketierter Integrationsstand verbindet die Controllergrenze mit dem echten begrenzten Runner ausschließlich über harmlose Python-Testprozesse. **41 Tests bestanden zweimal vollständig**, darunter neun neue Integrationstests; vier sequenzielle RED/GREEN-Zyklen sind belegt. Transportausnahmen einschließlich Timeouts werden zu einer bereinigten `HardwareStateUnknown`-Ausnahme. Auch Logsnapshots und Sitzungsabfragen verwenden diese Grenze. Ein während des Startversuchs auftretender Transportfehler persistiert `transport-unknown`, ohne Entladen, Reset oder Wiederholung; der zweite Start erzeugt keinen weiteren Prozess. Der normale Erfolgsfall der synthetischen Probe bleibt getestet. Produktive Preflight- und Readinessfunktionen sind unverändert; die CLI verweigert weiterhin mit Exit 2 ohne Effekte. Das ist weder eine sichere native Verdrahtung noch Hardwareevidenz. In diesem ersten Stand waren Behebung und Abnahme des unabhängig gefundenen Runner-Unterbrechungsfehlers noch offen; der folgende Absatz dokumentiert die getrennte Korrektur. Executable-Admission, exklusiver Runtime-Lock, vollständige Verträge und SELinux bleiben offen. Die separate Runnerlizenz wird durch diese internen Tests nicht gewählt; es gibt kein kombiniertes öffentliches Archiv.

**Sicherheitsreview und lokale Korrektur:** Das unabhängige Review hat zwei ungeschützte Lebenszyklusfenster des ursprünglichen Runners nachgewiesen: Ein echtes SIGINT nach Spawn beziehungsweise vor Timeout-Cleanup entwich als roher `KeyboardInterrupt`; der Kindprozess lebte weiter, ohne Quarantäne, und ein zweiter Spawn war möglich. Beide Regressionen wurden unabhängig reproduziert. Der separate Korrekturkandidat bestand danach die eigenständige Parentprüfung mit **30 Tests**, einschließlich der ursprünglichen 18 und realer Unterbrechungs-/Cleanup-Regressionen. Ein neuer interner Offline-Integrationsstand übernimmt exakt diesen Runner bei bytegleichem Controller: **44 Tests bestanden zweimal vollständig.** Ein echter RED/GREEN-Zyklus belegt den Wechsel vom rohen `KeyboardInterrupt` zum bereinigten `HardwareStateUnknown`; zwei ergänzende Tests prüfen Cleanup-Eintritt und einen nach tatsächlichem Spawn nicht zurückgegebenen Handle mit `SystemExit`. Während eines Startversuchs werden `transport-unknown` und die Unknown-Flags persistiert; ein zweiter Controllerstart erzeugt keinen weiteren Prozess und keinen Unload-/Resetpfad. Bei unbekanntem Handle bleibt der Runner gesperrt; ausschließlich die äußere Testhülle kann ihr eigenes Kind bereinigen. Alle protokollierten Testhüllen-Cleanups wurden bestätigt. Alte Originale und der frühere Integrationsstand bleiben unverändert fehlerhaft; die neue Prüfung ist keine rückwirkende Abnahme dieser Stände. Native Preflight-/Readinessfunktionen bleiben unverändert. Keine Garantie gegen beliebige asynchrone Python-Ausnahmen oder harte OS-Zeitgrenzen, kein Hardwarequieszenznachweis und keine native Freigabe. Runnerlizenz, Executable-Admission, exklusiver Runtime-Lock und native Verträge bleiben getrennt offen.

**Exklusiver Lock lokal geprüft, Deployment weiter offen:** Eine weitere interne Erweiterung schützt den vollständigen Startversuch über einen nicht blockierenden Linux-`flock`, vor Preflight und Zustandsabfragen bis zur abschließenden Journalspeicherung. **56 Tests bestanden zweimal auch in einer separaten Parent-Abnahmekopie**, einschließlich 44 bestehender und zwölf neuer Tests. Echte Zwei-Prozess-Konkurrenz verweigert den zweiten Start vor jeder Boundary-Aktion und Journalanlage; Fehler- und Unterbrechungstests prüfen Freigabe und den erhaltenen persistenten Zweitstartschutz. Descriptor-relative No-Follow-Öffnungen, Eigentümer-/Modus-/Linkprüfungen und Inodeabgleich sind lokal geprüft. Der bisherige Controller-AST ist abgesehen von der neuen geschützten Einstiegsfunktion unverändert; Runner und vorhandene Tests sind bytegleich. Der Lock schützt nur kooperierende Aufrufer mit derselben stabilen Lockidentität. Sichere Provisionierung und Ancestry des vorab geöffneten Parentverzeichnisses sowie die verbindliche native Nutzung des geschützten Einstiegs sind nicht dadurch bewiesen. Direkte interne FSM-Aufrufe sind nicht verriegelt. Keine Hardwarequieszenzgarantie, keine native Startfreigabe; native Readiness-Gates und separate Runnerlizenz bleiben unverändert.

**Separate Python-Projektlizenz geklärt:** Die ursprüngliche Assistentengenerierung des internen Bootcontrollers wurde anhand der tatsächlichen Schreib-/Patchaufrufe bytegleich rekonstruiert. Eine kopierte fremde Python-Implementierung wurde nicht identifiziert; es werden ausschließlich Standardbibliotheken importiert, nicht deren Implementierungen gebündelt. Eine weltweite Originalitätsgarantie wird daraus nicht abgeleitet. Der Projektbetreiber hat ausdrücklich **GPL-2.0-only** für den projektspezifischen Controller samt Tests, Manifest, Templates und Herkunftshinweisen gewählt. Es wird keine persönliche Urheberschaft erfunden und keine fremde Lizenz geändert.

Das getrennte Quellarchiv `gpu-controller-source-gpl-v1.tar.gz` (SHA256 `8a51d669055a2136021cde9ebd897cb70a12ecc8dfe9e50a7ba087d7b9404248`) enthält zehn Dateien einschließlich vollständigem GPL-v2-Text und dokumentierter Lizenzwahl. Zwei Serialisierungen ergaben dieselben Archivbytes; alle Member stimmen mit den geprüften Quellen überein. Die drei Python-Dateien sind bis auf Lizenzkommentare AST-identisch zum zuvor geprüften Stand. **31 Offline-Tests bestanden erneut**, der Manifestcheck verweigert weiterhin mit Exitcode 2 ohne Effekte. Lizenzwahl und lokale Paketierung sind weder Veröffentlichung noch native Freigabe; das Archiv ist kein Bestandteil der sieben Kernel-/Modul-Kandidatenarchive.

Das aktuelle Folgearchiv `gpu-controller-source-gpl-v2.tar.gz` (SHA256 `dd432732698f82c02911c8ad77f60ac6dca51a0a64aacbbffcfd5df16179858e`) enthält elf Dateien. Hier wurde genau die inzwischen überholte Meldung `public-Python-license-grant-unresolved` aus der Readinessliste entfernt. Ein zuerst fehlgeschlagener und danach bestandener Regressionstest sichert die Statuskorrektur und den Fortbestand der nativen Sperrgründe. **32 Tests bestanden auch aus dem tatsächlich entpackten neuen Archiv.** Der AST-Vergleich bestätigt: Die vorhandene Controllerlogik unterscheidet sich ausschließlich durch den entfernten Listeneintrag; bisherige Tests, Manifest, Templates und GPL-Text sind bytegleich. `--check` endet weiterhin mit Exitcode 2, `effects_performed: false` und `runtime_observed: false`. Die Lizenzwahl umfasst weder fremde Komponenten noch den separaten Prozessrunner und hebt die native Startsperre nicht auf. Das erste Archiv bleibt als geprüfter Zwischenstand erhalten.

**Separate Runnerlizenz inzwischen gewählt:** Für den projektspezifischen Python-Runner einschließlich Korrekturen und zugehörigen projektspezifischen Tests/Begleitdateien wurde ausdrücklich **GPL-2.0-only** bestätigt. Die oben als offen bezeichnete Lizenzfrage betrifft die historischen Reviewstände. Ein neuer separater Quellkandidat `native-runner-source-gpl-v1.tar.gz` enthält sieben Dateien: die akzeptierte Runnerkorrektur, ursprüngliche Runnertests, Unterbrechungstests, deutschsprachige Hinweise, Lizenzentscheidung, Herkunftshinweise und vollständigen GPL-v2-Text. Alle drei Pythondateien unterscheiden sich ausschließlich durch den SPDX-Kommentar; der AST ist unverändert. Zwei deterministische Paketierungen sind bytegleich, alle Archivmember wurden gegen die Quellen geprüft. **26 Tests bestanden zweimal aus dem tatsächlich entpackten Archiv**, einschließlich bestätigtem Testhüllen-Reaping und Pipeabschluss. SHA256: `434b95aaf1a2c6ca113671518ed06151de725f4cfd252f9ce3755809624e7bd5`. Kein konkreter Fremdcodeimport wurde identifiziert; ein historischer Runner-Erstellungsreplay und eine weltweite Originalitätsgarantie werden nicht behauptet. Fremde Komponenten und private Evidenzlogs sind ausgeschlossen. Historische Originale, native Gates und die sieben Kernel-/Modularchive bleiben unverändert. Dies ist keine Lizenzwahl für weitere neue Module, keine Veröffentlichung, Installation oder native Freigabe.

Die zweistufige [Installationsanleitung](release-v1/INSTALLATION.de.md), [technische Pfadzuordnung](release-v1/INSTALLATION-TECHNIK.de.md), [Rückfallbeschreibung](release-v1/ROLLBACK.de.md) und [Abnahmecheckliste](release-v1/RELEASE-ABNAHME.de.md) dokumentieren diese Sperre ausdrücklich. Die Schritte sind noch kein ausgeführter Installer oder Startnachweis.

## 5. Erledigter Vorbereitungsstand und Schritte bis zum Download

1. **Vollständige Quellen lokal paketiert:** Für diesen Kandidaten sind exakte Basis und Änderungen, finale Konfiguration, zugehörige externe Module/Helfer, erforderliche Lizenzen und Buildunterlagen zusammengeführt und geprüft. Private Installationshelfer und vorhandene Initramfs bleiben ausgeschlossen.
2. **Rechte und Hinweise lokal geprüft:** Herkunft, Drittvermerke sowie eingebettete beziehungsweise generierte Daten sind für den abgegrenzten Sieben-Archiv-Kandidaten dateibezogen bewertet und die erforderlichen Hinweise enthalten. Diese Prüfung erteilt keine pauschale Freigabe weiterer Dateien.
3. **Bereinigter Releasebau abgeschlossen:** Der Kandidat verwendet die geprüfte öffentliche Buildidentität und Pfadbereinigung mit den oben dokumentierten Grenzen. Bestehende akzeptierte Artefakte bleiben unverändert; Signaturvertrauen für die native Installation ist weiterhin nicht validiert.
4. **Paket und Funktion getrennt bewerten:** Die unabhängige lokale Archiv-, Quellen-, Metadaten- und Modulprüfung ist abgeschlossen. Boot und Hardwareabnahme des Public-v1-Kandidaten bleiben offen; die native Installation bleibt gesperrt.
5. **Veröffentlichung separat entscheiden:** Geprüfte Binärdateien und vollständige passende Quellen gemeinsam mit ehrlichen experimentellen Grenzen anbieten. Ein vorheriger Bootversuch ist keine Voraussetzung für diese Veröffentlichung; eine native Installationsfreigabe folgt daraus nicht.

Audio bleibt ohne Wiedergabe, Kamera ohne native Aufnahme. Ein vorgezogenes Grafik-/USB4-Release müsste diese Grenzen ausdrücklich nennen und dürfte nicht als fertige Gesamtlösung bezeichnet werden.

## Nachweisgrenze

Interne Grundlage sind `kernel-release-audit-v1` und `module-release-audit-v1`; deren vollständige Auditdaten enthalten private Arbeitsreferenzen und werden nicht mitgeliefert. Unabhängig geprüft wurden die Hashes von 18 Kernel-Artefakt-Datensätzen, zwölf Moduldateien, 25 Quelleingängen und 313 Kernel-Auditdateien. Mehrere Datensätze können Kopien desselben Artefakts bezeichnen; das sind nicht 18 verschiedene Kernel.

Die öffentliche Seite beschreibt das konkrete Prüfergebnis und die verbliebenen Schranken. Sie ersetzt weder den gemeinsamen Download aller zugehörigen Releaseassets noch eine individuelle Rechtsberatung. Ein lokaler vollständiger Paketkandidat ist vorhanden; ein öffentlicher Downloadort und eine native Installationsabnahme sind damit nicht behauptet.
