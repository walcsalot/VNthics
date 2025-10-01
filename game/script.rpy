# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define father = Character("Ama", color="#c8ffc8")
define mother = Character("Ina", color="#ffc8c8")
define lola = Character("Lola Rosa", color="#ffc8ff")
define miguel = Character("Miguel", color="#c8c8ff")
define ana = Character("Ana", color="#c8ffff")
define maria = Character("Maria", color="#ffffc8")
define pedro = Character("Pedro", color="#c8ffff")
define guro = Character("Guro", color="#ffcc99")

define maestro = Character("Maestro Aurelio", color="#c8ffc8")
define isabel = Character("Isabel", color="#ffc8c8")
define benjo = Character("Benjo", color="#c8ffff")
define carla = Character("Carla", color="#ffcc99")
define liza = Character("Liza", color="#ffffc8")
define diego = Character("Diego", color="#c8c8ff")
define leo = Character("Leo", color="#ffc8ff")

define aling_nena = Character("Aling Nena", color="#FFFF00") # Yellow
define mang_tonyo = Character("Mang Tonyo", color="#00FF00") # Green
define clara = Character("Clara", color="#FF00FF") # Magenta
define benny = Character("Benny", color="#00FFFF") # Cyan
define father_michael = Character("Father Michael", color="#FF8800") # Orange

define althea = Character("Althea", color="#c8ffc8")
define nanay_cora = Character("Nanay Cora", color="#ffc8c8")
define tatay_ben = Character("Tatay Ben", color="#c8c8ff")
define lola_idad = Character("Lola Idad", color="#ffc8ff")
define g_santos = Character("G. Santos", color="#ffcc99")
define kaibigan1 = Character("Kaibigan 1", color="#c8ffff")
define kaibigan2 = Character("Kaibigan 2", color="#ffffc8")
define barangay_captain = Character("Barangay Captain", color="#c8ffff")

# quick_menu variable is defined in screens.rpy

# Initialize moral score (ONLY ONCE)
default moral_score = 0
default current_scenario = ""

# Authentication variables
default username = ""
default password = ""
default is_authenticated = False
default login_attempts = 0
default max_login_attempts = 100

# User storage (in a real application, this would be a database)
default registered_users = {
    "student": {
        "password": "vne2024",
        "email": "student@vne.com",
        "full_name": "Default Student",
        "created_date": "2024-01-01"
    }
}

# Default credentials (in a real application, these would be stored securely)
define default_username = "student"
define default_password = "vne2024"

# The game starts here
label start:
    # This label is called when starting a new game
    # Authentication is handled in the main_menu screen
    jump scenario1


# Main menu label - redirects to scenario selection
label main_menu:
    # Show the main menu screen (defined in screens.rpy). This ensures the
    # game opens at the full main menu rather than jumping directly to the
    # scenario selection screen.
    call screen main_menu
    return

# ------------------ SCENARIO 1: Filipino Story ------------------
label scenario1:
    $ moral_score = 0
    $ current_scenario = "scenario1"
    
    # Autosave when starting scenario
    $ custom_autosave_scenario_start("scenario1", "Filipino Story")

    scene entrance  
    with fade

    "Sa maliit na bayan ng San Isidro, nakatira ang pamilya Santos sa isang simpleng tahanan."
    "Sila ay binubuo nina Juan (ama), Maria (ina), Miguel (14 na taong gulang), Ana (12 na taong gulang), at Lola Rosa."

    show father at center
    father "Mga anak, ang buhay ay puno ng hamon, ngunit ang pamilyang nagmamahalan ay kayang lampasan ang anumang pagsubok."

    show mother at right
    mother "Tandaan ninyo, ang kayamanan ay hindi nasusukat sa pera kundi sa pagmamahal at respeto sa isa't isa."

    show lola at left
    lola "At huwag ninyong kalilimutan ang pananampalataya sa Diyos. Siya ang ating gabay sa lahat ng pagsubok."

    "Ang Pamilya Santos ay kilala sa kanilang kabutihan at pagtutulungan sa kanilang maliit na komunidad."
    "Bagamat hindi sila mayaman, puno ng pagmamahal at mga aral sa buhay ang kanilang tahanan."

    jump act1

# ------------------ ACT 1: ANG UMAGA ------------------
label act1:
    scene lounge 
    with fade

    "Maagang umaga sa tahanan ng mga Santos. Ang araw ay nagsisimula na at may mga gawaing naghihintay."

    show miguel at center
    miguel "Naku, alas-sais na pala ng umaga! Muntik na akong mahuli sa paggising."

    # Autosave before choice
    $ custom_autosave_choice("scenario1", 1, "Umaga na. Ano ang gagawin ni Miguel?")

    menu:
        "Umaga na. Ano ang gagawin ni Miguel?"
        
        "Bumangon nang maaga at tumulong sa mga gawaing bahay":
            $ moral_score += 1
            $ track_moral_choice("scenario1", 1, "Bumangon nang maaga at tumulong sa mga gawaing bahay", "Tumulong si Miguel sa paghahanda ng pagkain at pag-aayos ng bahay. Ikinatuwa ito ng kanyang mga magulang.", 1)
            miguel "Tutulungan ko si Nanay sa paghahanda ng almusal. Mahalaga ang pagtulong sa pamilya."
            "Tumulong si Miguel sa paghahanda ng pagkain at pag-aayos ng bahay. Ikinatuwa ito ng kanyang mga magulang."
            
        "Magpahinga pa at ipagpaliban ang pagtulong":
            $ moral_score -= 1
            $ track_moral_choice("scenario1", 1, "Magpahinga pa at ipagpaliban ang pagtulong", "Natulog pa si Miguel at nahuli sa pagtulong sa mga gawaing bahay. Ikinagalit ito ng kanyang ama.", -1)
            miguel "Limang minuto pa... antok na antok pa ako."
            "Natulog pa si Miguel at nahuli sa pagtulong sa mga gawaing bahay. Ikinagalit ito ng kanyang ama."

    "Pagkatapos ng almusal, naghanda na si Ana para pumasok sa eskwelahan."

    show ana at right
    ana "Paalam po! Mag-iingat po kayo."

    jump act2

# ------------------ ACT 2: PAGKAKAMALI NI MIGUEL ------------------
label act2:
    scene hi
    with fade

    "Pagkatapos ng klase, naglaro si Miguel at ang kanyang mga kaibigan sa palaruan."

    show miguel at left
    miguel "Tara, laruin natin ang bagong laruan ni Pedro!"

    "Masayang naglaro ang mga bata hanggang sa may nangyari ng di inaasahan."

    "*CRACK*"

    show pedro at right
    pedro "Naku! Ang laruan ko! Nabasag!"

    "Aksidenteng nabasag ni Miguel ang mamahaling laruan na regalo kay Pedro sa kanyang kaarawan."

    menu:
        "Ano ang gagawin ni Miguel?"
        
        "Itago at itanggi ang pagkakamali":
            $ moral_score -= 1
            miguel "Hindi ko sinasadya... baka hindi niya malaman na ako ang may gawa."
            "Itinago ni Miguel ang totoo, ngunit siya ay nabagabag at hindi makatulog sa gabi."
            "Nakaramdam ng guilt at takot na malaman ang katotohanan."
            
        "Umamin at humingi ng tawad nang taos-puso":
            $ moral_score += 1
            miguel "Pedro, ako ang nakabasag. Pasensya na talaga. Hahanap ako ng paraan para mapagawa ito."
            "Bagamat nalungkot si Pedro, hinangaan niya ang katapatan ni Miguel."
            "Nagkasundo silang ayusin ang laruan at naging mas matibay ang kanilang pagkakaibigan."

    jump act3

# ------------------ ACT 3: PAGSUBOK SA TRABAHO ------------------
label act3:
    scene dining_kitchen
    with fade

    "Isang linggo ang lumipas, may mas malaking pagsubok ang dumating sa pamilya Santos."

    show father at center with dissolve
    father "Maria, may masama akong balita. Nawalan ako ng trabaho sa pabrika."

    show mother at right with dissolve
    mother "Ano? Paano na tayo? Paano na ang mga anak natin?"

    "Biglang bumigat ang kapaligiran sa maliit nilang tahanan. Ang kita ni Juan ang pangunahing pinagkukunan ng pamilya."

    show lola at left with dissolve
    lola "Huwag kayong mawalan ng pag-asa. Sa lahat ng unos, ang pananampalataya at pagtutulungan ang ating sandigan."

    menu:
        "Paano tutugon ang pamilya sa pagsubok na ito?"
        
        "Magreklamo at magsisihan":
            $ moral_score -= 1
            father "Bakit palaging ganito ang buhay? Hindi ko na alam ang gagawin!"
            mother "Wala na tayong pera para sa pagkain at upa! Paano na ang mga bata?"
            "Nagaway ang mag-asawa at lumala ang tensyon sa bahay. Nadama ng mga bata ang bigat ng problema."
            
        "Magkaisa at humanap ng solusyon nang magkasama":
            $ moral_score += 1
            father "Laban tayo! Maghahanap ako ng bagong trabaho. Samantala, magtipid tayo."
            mother "Tama ka. Magtutulong-tulong tayo. Ako'y magluluto ng mga pagkaing pwedeng ibenta."
            "Nagkaisa ang pamilya at naghanap ng mga paraan para makaraos sa kahirapan."

    jump act4

# ------------------ ACT 4: MGA TUksO ------------------
label act4:
    scene outside2
    with fade

    "Dahil sa kahirapan, naging vulnerable si Miguel sa mga tukso."

    "Isang araw, inaya siya ng mga batang lansangan na magnakaw sa malaking tindahan."

    show miguel at center
    miguel "Hindi, ayaw ko. Mali ang magnakaw."

    "Ngunit patuloy silang nambubuyo..."

    menu:
        "Ano ang gagawin ni Miguel?"
        
        "Sumama at magnakaw para may maibigay sa pamilya":
            $ moral_score -= 2
            miguel "Siguro... kailangan naming kumain. Baka makatulong ito."
            "Sumama si Miguel, ngunit nahuli sila ng guwardiya. Dinala sila sa pulisya at napahiya ang buong pamilya."
            
        "Tumanggi at manindigan sa tama":
            $ moral_score += 1
            miguel "Hindi ko ito gagawin! Kahit gaano kami kahirap, hindi magnanakaw ang pamilya namin!"
            "Umalis si Miguel at imbes na magnakaw, naghanap siya ng mga parol na pwede niyang gawin at ibenta."

    "Samantala, may nag-alok kay Juan ng trabaho..."

    show father at center
    father "May nag-alok sa akin ng trabaho. Malaki ang sahod, ngunit ilegal ang gagawin."

    menu:
        "Ano ang gagawin ni Juan?"
        
        "Tanggapin ang ilegal na trabaho para sa pamilya":
            $ moral_score -= 2
            father "Kahit paano, may pagkain na sa mesa. Wala na akong choice."
            "Ngunit nagdulot ito ng pangamba at kahihiyan sa pamilya. Lalong naging mahirap ang sitwasyon."
            
        "Tanggihan at manatiling tapat sa prinsipyo":
            $ moral_score += 1
            father "Hindi ko ipagpapalit ang dangal ng pamilya sa pera. May ibang paraan."
            "Bagamat naghirap sila nang sandali, nanatili ang kanilang dignidad at respeto ng komunidad."

    jump act5

# ------------------ ACT 5: ANG BAGYO ------------------
label act5:
    scene bg storm
    with fade

    "Habang patuloy na humaharap sa pagsubok ang pamilya, dumating ang mas malaking hamon."

    "Isang malakas na bagyo ang tumama sa kanilang bayan. Malakas ang ulan at hangin."

    show mother at right
    mother "Naku! Bumabaha na! Kailangan nating lumikas!"

    "Biglang may narinig silang sigaw mula sa kapitbahay."

    "TULONG! NASUSUNOG ANG BAHAY NAMIN! MAY NASA LOOB PA!"

    menu:
        "Ano ang gagawin ng pamilya?"
        
        "Tumulong sa kapitbahay kahit may panganib":
            $ moral_score += 1
            father "Juan, samahan mo akong tumulong! Maria, ilikas mo ang mga bata!"
            "Tumulong ang pamilya Santos sa pagliligtas ng kanilang kapitbahay. Nakaligtas ang buong pamilya mula sa nasusunog na bahay."
            
        "Iligtas lamang ang sarili at ang kanilang gamit":
            $ moral_score -= 1
            father "Unahin natin ang sarili natin! Hindi tayo puwedeng magpanganib!"
            "Nakaligtas ang pamilya Santos, ngunit nasunog ang bahay ng kapitbahay at may nasugatan."

    "Pagkatapos ng bagyo, may isa pang mahalagang pagpapasya si Ana."

    show ana at center
    ana "May scholarship exam ako bukas. Makakapag-aral ako nang libre kung papasa ako."
    ana "Ngunit kailangan ng pamilya ng tulong ko sa pag-aayos ng bahay at paghahanap-buhay."

    menu:
        "Desisyon ni Ana"
        
        "Tumulong muna sa pamilya at isakripisyo ang exam":
            $ moral_score += 1
            ana "Pamilya muna. Maaari akong sumubok muli sa susunod na taon."
            "Tumulong si Ana sa pamilya at nakahanap ng mga paraan para kumita. Ikinagalak ito ng kanyang mga magulang."
            
        "Magpokus sa pagsusulit at ipagpaliban muna ang pagtulong":
            $ moral_score += 0
            ana "Kailangan kong magsikap para sa pamilya. Ang edukasyon ang sagot sa aming kahirapan."
            "Nag-aral si Ana at pumasa sa exam. Nakatulong ito sa kanila sa pangmatagalan."

    jump filipino_ending

# ------------------ MGA WAKAS ------------------
label filipino_ending:
    if moral_score <= -2:
        jump bad_ending
    elif moral_score in [-1, 0, 1]:
        jump neutral_ending
    elif moral_score >= 2:
        jump good_ending

label bad_ending:
    scene  home_dark
    with fade
    "Dahil sa mga maling desisyon, unti-unting nagkawatak-watak ang pamilyang Santos."
    "Ang kawalan ng respeto, pananampalataya, and pagtutulungan ay nagpatunay na ang mga maling pagpili ay nagdudulot ng kapahamakan."
    "Nawala ang init at pagmamahalan sa kanilang tahanan."
    "Ngunit hindi pa huli ang lahat. May pag-asa pa ring magbago at magsimula muli."
    jump main_menu

label neutral_ending:
    scene home_evening
    with fade
    "Nakaraos ang pamilyang Santos sa mga pagsubok, ngunit may mga sugat na hindi agad gumaling."
    "Natutunan nilang magtulungan at magtiwala sa isa't isa, ngunit may mga pagkakataong nagkakaroon pa rin ng alitan."
    "Patuloy silang nagsusumikap at umaasa na sa hinaharap, mas magiging maayos ang kanilang buhay."
    "Ang kahirapan ay hindi hadlang sa pagmamahalan, ngunit nangangailangan ito ng tibay ng loob at pagtitiis."
    jump main_menu

label good_ending:
    scene lounge
    with fade
    "Sa kabila ng mga pagsubok, lumakas at tumibay ang pamilyang Santos."
    "Ang kanilang pagtitiwala sa isa't isa, pananampalataya sa Diyos, at pagiging matatag sa harap ng hamon ay nagbunga ng magandang kinabukasan."
    "Natuto si Juan at Maria na magnegosyo ng maliit na carinderia, si Miguel ay naging responsable at masunuring anak,"
    "at si Ana ay nakapag-aral nang mabuti at nakatulong sa pamilya."
    "Napatunayan nilang ang tunay na kayamanan ay nasa puso't isipan, hindi sa pera o materyal na bagay."
    "Ang kanilang kuwento ay naging inspirasyon sa buong komunidad."
    jump main_menu

# ------------------ SCENARIO 2: ANG HARDIN NG PAGPAPAHALAGA ------------------

# Declare background images
image bg classroom1 = "BG/classroom1.png"
image bg hallway = "BG/hallway.png"
image bg hallway1 = "BG/hallway1.png"
image bg clubroom1 = "BG/smp_club1_day1.png"

# Declare ending images
image ending_good = "ending_good.png"
image ending_bad = "ending_bad.png"
image ending_neutral = "ending_neutral.png"

label scenario2:
    $ moral_score = 0
    
    scene bg classroom1
    with fade

    "Pahilis na humigop ang sikat ng araw sa mga bintana ng silid-aralan ni Maestro Aurelio, na nagliliwanag sa mga partikulo ng alikabok na sumasayaw sa hangin."
    "Unang araw iyon ng pagdiriwang ng Linggo ng Wika, at ang buong silid ay buzz ng sabik at kabang pagsasalu-salo."
    "Sa gitna ng lahat ay naroon ang kanilang guro, si Maestro Aurelio, isang lalaking mabait ang mata na naniniwalang ang mga aralin ay lumalawak nang higit pa sa mga textbook."

    show maestro at center
    maestro "Class, ang aming proyekto para sa linggong ito ay hindi simpleng report lamang. Ito ay isang puno."
    maestro "Ang bawat isa sa inyo ay kakatawan sa isang pangunahing pagpapahalaga, isang ugat na nagpapatibay sa ating bansa."
    maestro "Magtutulungan tayong magtayo ng isang 'Hardin ng Pagpapahalaga' para sa ating school fair."

    "Itinakda niya ang mga pagpapahalaga, at ang isang grupo ng pitong magkakaaibigan ay natagpuang magkakadugtong na dahil sa iisang layunin."

    "Si Miguel, isang konsideradong batang laging nakikita ang mabuti sa bawat sitwasyon, ay tinanggap ang Mapagpasalamat."
    "Si Isabel, palaging magalang at maalalahanin, ang sagisag ng Magalang."
    "Si Benjo, ang president ng klase, ang halatang pinili para sa Mapanagutan."
    "Si Carla, na kilala sa kanyang tahimik na lakas ng loob, ang puso ng Pananampalataya."
    "Si Liza, na laging may imaculadong uniporme at organisadong mga note, siya ang Malinis."
    "Si Diego, na may pagmamalaking nagkukuwento tungkol sa kasaysayan at mga bayani ng Pilipinas, siya ang Nasyonalismo."
    "At panghuli, si Leo, ang matalik na kaibigan ni Miguel. Si Leo, na kamakailan lamang ay muling nanirahan sa probinsya pagkatapos ng mga taon sa abroad, ay nahihirapan sa kanyang pagka-Pilipino."

    show leo at left
    show maestro at right
    "Nagulat ang lahat, pati na siya mismo, nang ibigay din sa kanya ni Maestro Aurelio ang Mapagpasalamat."
    maestro "Minsan, kailangan nating matutong makita kung ano ang dapat nating pasalamatan bago tayo tunay na mamukadkad."

    "Ang kanilang gawain ay gumawa ng isang display: isang malaking kahoy na puno kung saan ang bawat pagpapahalaga ay isang dahon, na kasama ng isang maikling kuwento kung paano nila ito isinabuhay."

    jump sc2_act1

# ------------------ ACT 1: MGA PAGPAPAHALAGA ------------------
label sc2_act1:
    scene bg classroom1
    with fade

    "Nagsimula nang maayos ang linggo."

    show isabel at center
    isabel "Mga kaibigan, magsimula tayo sa pagpaplano. Bawat isa ay magkakaroon ng pagkakataong magsalita."
    "Si Isabel (Magalang) ay nagsaayos ng kanilang mga pagpupulong nang may malinis na paggalang, tinitiyak na ang bawat isa ay nabigyan ng pagkakataong magsalita."

    show benjo at right
    benjo "Gumawa ako ng checklist and timeline. Miguel, ikaw ang bahala sa mga dahon. Liza, ikaw sa mga materyales."
    "Si Benjo (Mapanagutan) ay gumawa ng checklist and timeline, na nagde-delegate ng mga gawain nang patas."

    show liza at left
    liza "Panatilihin nating malinis ang workspace. Magtapon ng basura sa tamang lalagyan."
    "Si Liza (Malinis) ang namahala sa mga kagamitan, pinapanatiling malinis ang kanilang workspace, nangongolekta ng mga scrap, at paalala sa lahat na maglinis."

    show diego at center
    diego "Magandang ideya na gumamit tayo ng mga katutubong materyales—mga dahon ng anahaw para sa puno at banig para sa background."
    "Si Diego (Nasyonalismo) ay nagmungkahi na gumamit sila ng mga katutubong materyales."

    "Subalit may problemang umusbong kay Leo. Siya ay nanlulumo at tahimik."

    show leo at left
    leo "Bakit ko kailangang maging mapagpasalamat? Papasalamat ba ako na umalis ako sa dati kong school? Ni hindi ko nga ramdam na Pilipino ako. Hindi ako makakasulat ng kuwento tungkol dito."

    menu:
        "Ano ang dapat gawin ni Miguel?"
        
        "Hayaan muna si Leo at mag-focus sa sariling gawain":
            $ moral_score -= 1
            show miguel at right
            miguel "Sige, pag-isipan mo muna yan Leo. Ako muna ang magtatrabaho sa mga dahon."
            "Hindi na nakialam si Miguel at nag-focus sa kanyang sariling gawain. Mas lalong naging malungkot si Leo."
            
        "Kausapin at bigyan ng suporta si Leo":
            $ moral_score += 1
            show miguel at right
            miguel "Nagpapasalamat ako sa proyektong ito dahil pinagsama-sama tayo nito. At nagpapasalamat ako na kaibigan kita, Leo. Malulutas natin ito."
            "Naramdaman ni Leo na may nagmamalasakit sa kanya at bahagyang gumaan ang kanyang pakiramdam."

    show carla at center
    carla "Magkaroon ka ng pananampalataya, Leo. Hindi lang sa Diyos, kundi sa sarili mo at sa amin. Darating din ang sagot."

    jump sc2_act2

# ------------------ ACT 2: ANG SAKUNA ------------------
label sc2_act2:
    scene bg hallway1
    with fade

    "Kalagitnaan ng linggo, dumating ang malaking sakuna."
    "Habang tanghalian, isang malakas na hanging umihip sa kanilang nakabukas na bintana sa silid-aralan."
    "Ang kanilang halos tapos nang puno, kasama ang maingat na nilikha nilang mga dahon, ay pinagpag ng hangin."
    "Ang mga pots ng pintura ay tumapon, nagkalat ng maliwanag na kulay sa kanilang backdrop na banig at sa mga kuwentong kanilang sinulat."
    "Ang magandahang hardin ay naging isa nang madungis, makulay na gulo."

    "Nakatayo ang grupo sa pagkagimbal."

    show benjo at center
    benjo "Kasalanan ko ito. Dapat ay mas secure ko ang base. Ako ang may pananagutan dito."

    show liza at right
    liza "Nasira ito. Lahat ng ating pinaghirapan..."

    menu:
        "Paano dapat tumugon si Diego sa sitwasyon?"
        
        "Sumama sa pagkabigo at sisihin ang iba":
            $ moral_score -= 1
            show diego at left
            diego "Bakit hindi natin sinara ang bintana? Dapat may nag-isip niyan!"
            "Nagkaroon ng tensyon sa grupo at mas lalong nawalan ng pag-asa ang mga mag-aaral."
            
        "Magpakita ng bayanihan at magbigay ng inspirasyon":
            $ moral_score += 1
            show diego at left
            diego "Mas malalaking problema ang hinarap ng ating mga bayani kaysa dito! Hindi sila sumuko. Spirit ng bayanihan, everyone! Maayos natin ito."
            "Nagkaroon ng bagong lakas ng loob ang grupo sa mga sinabi ni Diego."

    show isabel at center
    isabel "Tama si Diego. Huwag nating sisihin ang sinuman. Magtulungan tayo nang magalang."

    jump sc2_act3

# ------------------ ACT 3: PAGBABAGONG-LOOB NI LEO ------------------
label sc2_act3:
    scene bg hallway 
    with fade

    "Mabilis silang kumilos."

    show liza at center
    liza "Ako na ang bahala sa paglilinis. May alam akong paraan para matanggal ang mga batik ng pintura."
    "Pinangunahan ni Liza (Malinis) ang operasyon ng paglilinis nang mahusay, ipinakita na ang tunay na kalinisan ay tungkol sa pagpapanumbalik ng kaayusan, hindi lamang pagpapanatili nito."

    show benjo at right
    benjo "Gagawin kong mas matatag ang base ng puno. Hindi na ito matutumba."
    "Buong-pananagutang pinamunuan ni Benjo (Mapanagutan) ang pagsisikap na muling itayo ang base ng puno, ginawa itong mas matatag ngayon."

    show carla at left
    carla "Kaya natin ito! Magtulungan lang tayo."
    "Si Carla (Pananampalataya) ay lumibot sa kanila, nag-aalok ng mga salita ng pag-encourage."

    menu:
        "Ano ang dapat gawin ni Miguel?"
        
        "Mag-focus lang sa sariling gawain at hindi isipin ang iba":
            $ moral_score -= 1
            show miguel at center
            miguel "Ako na lang ang magpapatuloy sa mga dahon. Sana matapos ko ito sa oras."
            "Nag-focus si Miguel sa kanyang sarili at hindi niya napansin na nangangailangan ng tulong ang kanyang mga kaibigan."
            
        "Magpakita ng pasasalamat at magbigay ng suporta sa lahat":
            $ moral_score += 1
            show miguel at center
            miguel "Nagpapasalamat ako na magkakasama tayong team. Nag-uwi ako ng meryenda para sa lahat."
            "Tumakbo si Miguel (Mapagpasalamat) sa canteen at nag-uwi ng meryenda para sa lahat, na nagpapasalamat sa kanilang pagsusumikap."

    "Lahat maliban kay Leo, na nakaupo sa sulok, nanonood. Nakita niya ang kanyang mga kaibigan, na puno ng pintura and pawis, ngumingiti ngayon habang ginagawa nilang hamon ang sakuna."

    menu:
        "Ano ang dapat gawin ni Leo?"
        
        "Manatili sa sulok at hintayin matapos ang lahat":
            $ moral_score -= 1
            "Nanatili si Leo sa kanyang kinaroroonan, nakikita ang kanyang mga kaibigan na nagtutulungan habang siya ay nanonood lamang."
            "Naramdaman niyang hindi siya kabilang at mas lalong nawalan ng pag-asa."
            
        "Sumali at tumulong sa paggawa ng proyekto":
            $ moral_score += 1
            show leo at center
            leo "Gagawin ko. Isusulat ko ang aking kuwento. At tutulong akong magrepaint."
            "Nakahanap siya ng bago, malinis na dahon at brush. Habang itinutayo ng kanyang mga kaibigan ang puno, nagsimulang magpinta at sumulat si Leo."

    jump sc2_ending

# ------------------ WAKAS ------------------
label sc2_ending:
    if moral_score >= 2:
        jump sc2_good

    elif moral_score in [-1, 0, 1]:
        jump sc2_neutral

    elif moral_score <= -2:
        jump sc2_bad
    
    
    label sc2_good:
        scene bg classroom1
        with fade
        "Sa araw ng fair, ang kanilang 'Hardin ng Pagpapahalaga' ay proud na nakaposisyon sa gymnasium."
        "Ito ang pinakamagandang display, hindi dahil ito ay perpekto, kundi dahil ang kuwento nito ay nakaukit sa bawat stroke."
        # ... (Leo’s inspiring speech kept the same)
        show maestro at center
        maestro "Natutunan ninyo na ang mga pagpapahalagang ito ay hindi lamang mga salita sa isang pahina; ang mga ito ay buhay..."
        "Nagtanim sila ng isang hardin, at sa paggawa nito, ay hinayaan ang kanilang sariling mga diwa na mag-ugat at lumago."
        return 

    label sc2_bad:
        scene bg classroom1
        with fade
        "Ngunit sa kasamaang-palad, ang kanilang proyekto ay hindi gaanong naging maganda dahil sa kawalan ng pagtutulungan."
        "Ang mga dahon ay hindi magkakatugma at ang puno ay mukhang hindi pinag-isipan."
        "Si Leo ay hindi nakapagbahagi ng kanyang kuwento dahil hindi niya ito natapos."
        "Nagtapos ang Linggo ng Wika na may hindi magandang karanasan para sa grupo."
    jump main_menu

    label sc2_neutral:
        scene bg classroom1
        with fade
        "Ang kanilang proyekto ay naging maayos ngunit may mga kakulangan pa rin."
        "Nakapagbahagi si Leo ng kanyang kuwento ngunit kulang sa kumpyansa at sigla."
        "Natuto ang grupo ng mahahalagang aral ngunit may mga pagkakataong hindi sila nagkasundo."
    jump main_menu
        
# --- SCENARIO 3: ANG PUSO NG BARANGAY PAG-ASA ---

label scenario3:
    $ moral_score = 0
    
    scene bg home_day
    with fade
    "Sa tahimik at makulay na Barangay Pag-asa, kung saan ang bawat pamilya ay tila isang malaking angkan, matatagpuan ang isang munting hardin."
    "Ito ang Hardin ni Aling Nena, isang matandang babae na ang mga ngiti ay kasing init ng araw, at ang payo ay kasing lamig ng hangin sa gabi."
    "Ang hardin na ito ang pinagmumulan ng sariwang gulay at prutas para sa karamihan sa barangay, lalo na sa mga nangangailangan."

    "Ngunit sa paglipas ng panahon, at dahil sa kanyang edad at karamdaman, unti-unting napabayaan ang hardin."
    "Ang mga gulay ay nalalanta, ang mga damo ay lumalago, at ang dating masaganang taniman ay tila nalulunod sa kalungkutan."

    show aling_nena at center
    "Isang umaga, habang pinagmamasdan ni Aling Nena ang kanyang hardin mula sa kanyang bintana, may lungkot sa kanyang mga mata."
    aling_nena "Kaytagal nang walang nag-aalaga sa aking hardin. Paano na ang mga bata na umaasa sa aking mga gulay?"

    hide aling_nena
    scene bg town_square_day
    with fade
    "Nakarating ang balita kay Mang Tonyo, ang aktibo at masigasig na kapitan ng barangay."
    show mang_tonyo at center
    mang_tonyo "Kailangan nating kumilos! Hindi maaaring pabayaan ang hardin ni Aling Nena. Ito ang puso ng ating barangay!"

    "Nagpatawag si Mang Tonyo ng pulong sa plasa ng barangay."
    "Maraming tao ang dumalo, bawat isa ay may kanya-kanyang ideya at damdamin tungkol sa sitwasyon."

    menu:
        "Paano dapat lapitan ang problema ni Aling Nena at ang pagpapanumbalik ng hardin?"
        "Magalang na kausapin si Aling Nena at humingi ng pahintulot":
            $ moral_score += 1
            mang_tonyo "Huwag nating madaliin. Dapat muna nating kausapin si Aling Nena nang buong paggalang, tanungin kung ano ang kanyang nais at kung paano tayo makatutulong."
            "Pinakinggan ng lahat ang payo ni Mang Tonyo. Nagpunta sila sa bahay ni Aling Nena, and matapat na ipinaliwanag ang kanilang hangarin."
            "Natuwa si Aling Nena at buong puso silang pinayagan."
        "Agad-agad simulan ang paglilinis nang hindi na nagpaalam pa":
            $ moral_score -= 1
            mang_tonyo "Wala nang oras para sa paliwanagan! Simulan na natin ang paglilinis! Kailangan ng agarang aksyon!"
            "Agad na sinimulan ng ilan ang paglilinis, ngunit nalito at nalungkot si Aling Nena. Naramdaman niyang hindi siya iginalang."

    "Anuman ang naging desisyon, nagsimula ang barangay sa pagpapanumbalik ng hardin. Nagtulungan ang bawat isa, bata at matanda."

    scene bg garden_day
    with fade
    "Habang nagtatrabaho, iba't ibang personalidad ang lumabas."
    show benny at left
    show clara at right
    "Si Benny, isang binata na kilala sa kanyang pagiging maagap ngunit minsan ay mainitin ang ulo, ay mabilis kumilos."
    "Si Clara naman, isang estudyante na puno ng pagmamalasakit, ay maingat at matiyaga sa kanyang bawat gawain."

    menu:
        "May nagkaroon ng hindi pagkakaintindihan sa pagitan nina Benny at isang kasama. Ano ang dapat gawin?"
        "Pagsabihan agad si Benny at piliting sundin ang proseso":
            $ moral_score -= 1
            clara "Benny, kailangan nating sundin ang plano. Huwag kang padalos-dalos."
            "Nagkaroon ng tensyon sa pagitan nila, at bahagyang bumagal ang trabaho dahil sa hindi pagkakasundo."
        "Mapagpasensiyang ipaliwanag ang kahalagahan ng pagtutulungan at kaayusan":
            $ moral_score += 1
            clara "Benny, alam kong gusto mong matapos agad, pero mas maganda kung magtutulungan tayo nang maayos para walang masira at mas mabilis ang trabaho. Konting pasensiya lang."
            "Naunawaan ni Benny ang sinabi ni Clara. Nagpatuloy sila sa trabaho nang mas payapa at organisado."

    "Ilang araw ang lumipas, at unti-unting nabubuhay muli ang hardin. Ngunit isang gabi, bumuhos ang malakas na ulan at kasabay nito ang malaking pagsubok."

    scene bg garden_storm
    with flash
    "Kinabukasan, ang hardin ay tila dinaanan ng bagyo. Ang ilang bagong tanim ay inanod, at ang mga suporta sa halaman ay nawasak."

    show benny at left
    show clara at right
    benny "Naku po! Ang lahat ng ating pinaghirapan... nasira!"
    clara "Huwag tayong mawalan ng pag-asa. May paraan pa."

    show father_michael at center
    father_michael "Mga anak, sa panahon ng pagsubok, higit nating kailangan ang pananampalataya. Hindi lamang sa Diyos, kundi sa ating sarili at sa kakayahan nating bumangon."

    menu:
        "Paano tutugon ang komunidad sa pagsubok na ito?"
        "Mawalan ng pag-asa at sumuko na lang":
            $ moral_score -= 1
            benny "Wala na ito. Hindi na natin kaya. Buong gabi tayong nagtrabaho, pero wala na."
            "Nawalan ng pag-asa ang ilan at tila nawalan ng direksyon ang proyekto."
        "Manalig at magtulungan muli nang may pananampalataya":
            $ moral_score += 1
            clara "May awa ang Diyos! Kailangan nating manalig at magtulungan muli. Magagawa natin ito!"
            father_michael "Tama si Clara. Ang pananampalataya ang magiging ilaw natin sa gitna ng dilim."
            "Nagkaisa ang lahat. Mas matatag ang kanilang loob at mas matibay ang kanilang pananampalataya."

    "Sa kabila ng pagsubok, hindi sumuko ang Barangay Pag-asa. Pinatunayan nilang ang pagtutulungan at pananampalataya ang sandigan nila."
    "Habang abala ang lahat sa pag-aayos ng hardin, napansin ni Clara na si Aling Nena ay tila humina na. Kailangan niya ng agarang tulong."

    scene bg aling_nena_house_interior
    with dissolve
    show clara at center
    "Hindi nag-atubili si Clara. Alam niyang kailangan niyang ipakita ang pagmamalasakit."
    clara "Kailangan kong tulungan si Aling Nena. Hindi niya kayang mag-isa."

    menu:
        "Paano tutulungan ni Clara si Aling Nena habang abala ang iba?"
        "Unahin ang sariling gawain sa hardin dahil doon siya naka-assign":
            $ moral_score -= 1
            clara "Mahalaga ang hardin, kaya kailangan kong tapusin ito. Baka may ibang makatulong kay Aling Nena."
            "Bagamat nakatulong siya sa hardin, naramdaman ni Aling Nena ang kaunting pagkabigo dahil sa kakulangan ng personal na atensyon."
        "Ipakita ang tunay na Mapagmalasakit at bisitahin si Aling Nena":
            $ moral_score += 1
            clara "Ang pagmamalasakit sa kapwa ay mas mahalaga. Sandali akong aalis sa hardin upang bisitahin si Aling Nena."
            "Dinalhan ni Clara si Aling Nena ng mainit na sabaw at kinausap ito nang matagal. Gumaan ang pakiramdam ni Aling Nena."

    "Nagtuloy ang pag-aayos ng hardin. Isang malaking bato ang bumara sa daluyan ng tubig, na nagiging sanhi ng pagbaha sa isang bahagi ng hardin."

    scene bg garden_problem
    with hpunch
    show benny at center
    "Kailangan ng mabilis na desisyon at pagkilos."
    benny "Kailangan nating alisin agad ito!"

    menu:
        "Ano ang gagawin ni Benny sa sitwasyong ito?"
        "Maghintay ng tulong mula sa iba bago kumilos":
            $ moral_score -= 1
            benny "Masyadong mabigat ito. Maghintay muna tayo ng karagdagang tulong."
            "Lumala ang baha dahil sa pagkaantala, at mas maraming tanim ang nasira."
        "Agad na kumilos at humingi ng tulong habang ginagawa ang lahat ng makakaya (Maagap)":
            $ moral_score += 1
            benny "Ako na ang uumpisa! Kailangan ng agarang aksyon! Mang Tonyo, tulungan niyo po ako!"
            "Agad na kumilos si Benny, at sa tulong ng iba, mabilis nilang naalis ang bato. Nailigtas ang karamihan sa mga tanim."

    "Sa huling yugto ng pagpapanumbalik ng hardin, kinailangan ni Mang Tonyo na gumawa ng isang mahalagang desisyon para sa pangmatagalang kapakinabangan ng komunidad."
    "May dalawang opsyon: Gumamit ng murang abono na pansamantala lang ang bisa, o mamuhunan sa organikong abono na mas mahal ngunit mas matagal ang epekto at mas ligtas sa kalikasan."

    scene bg town_square_evening
    with dissolve
    show mang_tonyo at center
    "Pinag-isipan ni Mang Tonyo ang bawat detalye. Mahalaga ang maging Maingat sa desisyong ito."

    menu:
        "Ano ang magiging desisyon ni Mang Tonyo?"
        "Piliin ang murang abono para makatipid sa budget (Hindi Maingat)":
            $ moral_score -= 1
            mang_tonyo "Kailangan nating magtipid. Gagamitin natin ang murang abono. Bahala na sa susunod."
            "Sa simula, tila gumana ang mura. Ngunit sa paglipas ng panahon, bumalik ang problema ng hardin at mas lumaki ang gastos."
        "Mamuhunan sa organikong abono para sa pangmatagalang benepisyo (Maingat)":
            $ moral_score += 1
            mang_tonyo "Hindi natin pwedeng madaliin ito. Ang hardin na ito ay para sa kinabukasan ng ating mga anak. Mamumuhunan tayo sa organikong abono. Mas mahal, oo, ngunit mas ligtas at pangmatagalan."
            "Pinuri ng lahat ang desisyon ni Mang Tonyo. Sa simula, naging hamon ang gastusin, ngunit sa kalaunan, naging mas matatag at masagana ang hardin."

    "Sa wakas, natapos ang pagpapanumbalik ng Hardin ni Aling Nena. Mas maganda, mas masagana, at mas matatag kaysa dati."
    "Ang hardin ay hindi lamang naging pinagmumulan ng pagkain, kundi simbolo rin ng pagtutulungan, pagmamalasakit, paggalang, pagpapasensiya, pananampalataya, pagiging maingat, at pagiging maagap ng Barangay Pag-asa."

    scene bg garden_day
    with fade
    show aling_nena at center
    aling_nena "Salamat, mga anak. Pinatunayan ninyo na ang pagmamahalan at pagtutulungan ang tunay na yaman ng ating komunidad."

    if moral_score >= 4:
        "Ang Barangay Pag-asa ay naging inspirasyon. Ang kanilang hardin ay patunay na sa gitna ng anumang pagsubok, ang pagkakaisa at pagpapahalaga sa kapwa ay nagbubunga ng isang mas masagana at payapang buhay."
        "Ang bawat dahon, bawat bunga, ay kuwento ng Mapagmalasakit, Mapagpasensiya, Magalang, Pananampalataya, Maingat, and Maagap na mga puso."
    elif moral_score >= 0:
        "Bagamat maraming hamon ang hinarap, ang Barangay Pag-asa ay natuto ng mahahalagang aral. Ang hardin ay muling bumalik sa dating sigla, at ang komunidad ay patuloy na nagsusumikap na mas maging matatag sa mga susunod na panahon."
        "Ito ay paalala na ang paglalakbay sa pagpapahalaga ay isang patuloy na proseso."
    else:
        "Sa kabila ng kanilang mga pagsisikap, maraming aral ang hindi lubos na natutunan. Ang hardin ay naibalik, ngunit hindi kasing sigla ng dati, at ang ilang isyu sa komunidad ay nanatili. Isang paalala na ang mga pagpapahalaga ay kailangan ng patuloy na paglinang."
    
    "Ang kwento ng Barangay Pag-asa ay nagpapakita na ang tunay na yaman ay nasa puso't isipan, sa pagkakaisa, at sa pagmamahal sa kapwa."
    jump main_menu

# Ang Alay ni Althea
label scenario4:
    $ moral_score = 0
    
    scene bg home_interior_day
    with fade

    "Sa isang payak ngunit maayos na tahanan, nakatira si Althea kasama ang kanyang pamilya."
    "Ang kanyang tahanan ay puno ng pagmamahal at mga aral sa buhay."

    show althea at center
    althea "Nay, hirap na hirap po ako sa takdang-aralin namin kay G. Santos. Tungkol po sa pagpapakita ng nasyonalismo sa pang-araw-araw na buhay. Paano po ba 'yun?"

    show nanay_cora at right
    nanay_cora "Anak, 'di kailangang maging komplikado 'yan. Tignan mo ang tatay mo. Mapanagutan siya sa kanyang trabaho bilang karpintero."
    nanay_cora "Tapat at mahusay siyang gumawa, 'di nagdadaya sa sukat o sa gamit. 'Yun na 'yon."
    nanay_cora "Pagiging mapanagutan sa iyong gawain ay pagmamahal na rin sa bayan - pinatitibay mo ang ekonomiya sa pamamagitan ng iyong husay."

    show lola_idad at left
    lola_idad "Tama ang sinabi ng nanay mo, iha. Noong panahon namin, ang nasyonalismo ay nasa simpleng pagsuporta sa produkto ng kapwa Pilipino."
    lola_idad "Bumibili kami ng gulay sa katabing bukid, hindi sa malaking supermarket. Mas masarap ang kain kapag alam mong tinanim ng kapwa mo."

    althea "So, hindi po 'yun tungkol sa malalaking bagay? Hindi pagiging bayani?"

    lola_idad "Ay naku, hija! Ang bayani ay 'yung mga nagpapakita ng pagmamahal sa kapwa sa maliliit na paraan araw-araw."
    lola_idad "Katulad ng nanay mo. Mapagpasalamat siya sa biyayang dumarating, kahit na maliit."

    nanay_cora "At ikaw, Althea, ang pagiging masunurin mo sa amin, ang pagsisikap mo sa pag-aaral - para 'yun sa iyong kinabukasan."
    nanay_cora "At ang kinabukasan mo ay parte ng kinabukasan ng bayang ito. Kaya 'wag kang mawalan ng pag-asa. Lagi kang positibo sa buhay."

    "Si Althea ay tumango, ang kanyang isipan ay puno ng mga bagong pananaw."

    jump sc4_act2

# ------------------ ACT 2: ANG PAARALAN AT ANG HAMON ------------------
label sc4_act2:
    scene bg classroom_day
    with fade

    show g_santos at center
    g_santos "...kaya nga, mga mag-aaral, ang nasyonalismo ay hindi natatapos sa pag-awit ng Lupang Hinirang. Ito'y kumikilos. Ito'y may mapanagutan."
    g_santos "Paano ninyo ito maipapakita sa inyong komunidad?"

    "Ang klase ay tahimik. Marami ang nakatitig sa labas ng bintana."

    show althea at right
    althea "Ginoo, maaari po bang magpakita ng nasyonalismo sa pamamagitan ng pagtulong sa komunidad?"
    althea "Tulad ng paglinis sa paligid o pagtulong sa mga nangangailangan?"

    g_santos "Magandang simula 'yan, Althea! Oo. Ang pagiging mapagpasalamat sa ating kapaligiran at sa mga biyayang mayroon tayo ay maipapakita sa pamamagitan ng pangangalaga dito."

    scene bg barangay_street
    with fade
    "Pag-uwi ni Althea, nag-iisa siyang naglakad at minasdan ang kanilang barangay."
    "May nakita siyang mga batang naglalaro sa tabi ng isang maliit na tambak ng basura."
    "Sa isang sulok, may mga matatandang nakaupo na tila walang magawa."
    "Bigla, may kumirot sa kanyang puso. Naalala niya ang mga salita ng kanyang pamilya at ni G. Santos."

    jump sc4_act3

# ------------------ ACT 3: ANG MUNTING PROYEKTO NG PAG-ASA ------------------
label sc4_act3:
    scene bg home_dining
    with fade

    show althea at center
    althea "Tay, Nay, Lola, may ideya ako. Project po namin sa school."
    althea "Gusto ko pong mag-organize ng clean-up drive sa may plaza. At pagkatapos, magkaroon ng munting programa para sa mga batang kalye."
    althea "Pwede po bang tulungan ninyo ako?"

    show tatay_ben at right
    tatay_ben "Mapanagutan ka ba sa proyektong ito, Althea? Hindi ito magaan. Kailangan ng plano."

    menu:
        "Paano sasagutin ni Althea?"
        
        "Magduda at mag-alinlangan":
            $ moral_score -= 1
            althea "Hindi ko po alam kung kaya ko. Baka masyadong malaki ito para sa akin."
            "Nawalan ng kumpyansa si Althea at halos hindi na ituloy ang proyekto."
            
        "Manindigan at magpakita ng determinasyon":
            $ moral_score += 1
            althea "Opo, Tay. Gagawan ko po ng plano. Hihingi ako ng tulong sa aking mga kaibigan."
            "Nagpakita si Althea ng tapang at determinasyon."

    show nanay_cora at left
    nanay_cora "Suportahan natin siya, Ben. Ito na ang kanyang paraan ng pagpapakita ng pagmamahal sa komunidad."

    show lola_idad at right
    lola_idad "Ako ang magkukwento sa mga bata! Kwento ng mga bayani at ng mga alamat ng Pilipinas!"

    "Nagsimula si Althea. Kinausap niya ang kanyang mga kaibigan."

    scene bg school_hallway
    with fade
    show kaibigan1 at left
    show althea at center
    show kaibigan2 at right

    kaibigan1 "Clean-up drive? Ang init noon, Althea!"

    menu:
        "Paano hihikayatin ni Althea ang kanyang mga kaibigan?"
        
        "Sumuko at hindi na ituloy":
            $ moral_score -= 1
            althea "Oo nga no, mainit nga. Sige, hindi na lang natin itutuloy."
            "Nawalan ng oportunidad ang komunidad na magkaroon ng magandang proyekto."
            
        "Magpakita ng positivity at magbigay ng motivation":
            $ moral_score += 1
            althea "Mas mainit po ang pakiramdam kapag malinis at maganda ang ating paligid, 'di ba? Tapos, mag-iigawan tayo ng ice cream!"
            "Ang kanyang magiliw na pag-uudyok ay nakahikayat. Sinimulan nilang mag-ikot at humingi ng pahintulot."

    jump sc4_act4

# ------------------ ACT 4: ANG PAGKILOS AT ANG PAGTUTULUNGAN ------------------
label sc4_act4:
    scene bg barangay_plaza
    with fade

    "Dumating ang Sabado ng umaga. Ang buong pamilya ni Althea ay handang tumulong."
    "Si Tatay Ben ay mapanagutan; dinala niya ang mga gamit panglinis at mga lapis at papel para sa mga bata."
    "Si Nanay Cora at ang kanyang mga kaibigan ay naghanda ng simple ngunit masustansyang meryenda."
    "Si Lola Idad, na nakasakay sa isang upuan sa ilalim ng puno, ay handang magkwento."

    show althea at center
    althea "Maraming salamat po sa inyong pagtulong. Ito po ay maliit na paraan para maipakitang mahal natin ang ating komunidad. Simula ito ng pagbabago."

    menu:
        "Paano pamumunuan ni Althea ang clean-up drive?"
        
        "Magpabaya at hayaan na lang ang iba ang gumawa":
            $ moral_score -= 1
            "Hindi aktibo si Althea sa pangangasiwa. Nagulo ang mga volunteers at hindi gaanong naging epektibo ang clean-up."
            
        "Maging aktibo at mapanagutan sa pamumuno":
            $ moral_score += 1
            "Aktibong namuno si Althea. Nagbigay siya ng mga instruksyon at tinitiyak na maayos ang lahat."
            "Ang mga mag-aaral, sa pangunguna ni Althea, ay masunurin sa mga tagubilin."
            "May nagwalis, nagpulot ng basura, nag-alis ng mga damo."

    "Pagkatapos maglinis, nagsimula ang programa. Kumanta ang mga bata."
    "At si Lola Idad, sa kanyang magiliw na tinig, ay nagkwento ng alamat ng Maria Makiling."

    jump sc4_ending

# ------------------ WAKAS ------------------
label sc4_ending:
    scene bg barangay_plaza_clean
    with fade

    "Pagkatapos ng matagumpay na aktibidad, lahat ay pagod ngunit masaya."

    show barangay_captain at center
    barangay_captain "Althea, ang proyektong ito ay kahanga-hanga. Napakaganda ng naisip mo."
    barangay_captain "Nagpapakita ito ng tunay na diwa ng nasyonalismo - ang pag-aalaga sa isa't isa at sa lugar na ating kinabibilangan."

    show tatay_ben at right
    tatay_ben "Mapanagutan po kasi ang aking anak. Nangako siya, at tinupad."

    show nanay_cora at left
    nanay_cora "Salamat, anak. Ipinakita mo sa amin na ang pag-asa para sa mas magandahang bukas ay nasa kamay ng mga kabataang tulad mo."

    show lola_idad at center
    lola_idad "At dahil sa magiliw mong personalidad, marami kang nahikayat. Iyan ang lakas ng pagiging positibo."

    if moral_score >= 3:
        "Ang proyekto ni Althea ay hindi natapos noon. Ito ay naging simula."
        "Taon-taon, ang maliit na clean-up drive at story-telling session ay naging tradisyon na sa kanilang barangay."
        "Ito ay patunay na ang maliliit na hakbang, na ginagawa nang may pusong puno ng pagmamahal, ay maaaring magpapagulo ng malaking pagbabago."
    elif moral_score >= 0:
        "Bagamat may mga hamon, natapos pa rin ang proyekto. Ngunit hindi ito naging tradisyon at natigil pagkatapos ng isang beses."
        "Natuto si Althea na mahalaga ang consistency at patuloy na pagsisikap."
    else:
        "Dahil sa kawalan ng determinasyon at pagtutulungan, hindi gaanong naging matagumpay ang proyekto."
        "Ngunit natuto si Althea ng mahalagang aral tungkol sa pamumuno at pagtutulungan."

    "Ang kwento ni Althea ay nagpapakita na ang tunay na pagmamahal sa bayan ay nagsisimula sa tahanan, pinalalawak sa paaralan, at pinakikita sa komunidad."
    
    # Return to main menu instead of just ending
    return
