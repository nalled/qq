from telethon import TelegramClient, events
from random import choice as ch
from asyncio import sleep as sl
from datetime import datetime


shabl = ['ти голозадий син шалави закрий рило нахуй своє я ж тобі тут сраку єбав',
'слабак блядоруснявий я тобі тут ні шансу не залишу нахуй ',
'не вихрюкуй тут син шалави криворукий',
'я тобі тут мати шлюху єбашу голими руками ару',
'нахуй ти руснявий син шлюхи помер тут',
'свиня блядорила я тебе тут нахуй в жопу єбу',
'завали єбало своє свиня кривозуба нахуй і не пиши сюди взагалі',
'ти труслива сволота русняворила я тобі зараз твоє свинне рило переломаю',
'не помирай тут слабак єбаний',
'на хую ти відкинув копита русняві ару',
'який тобі нон стоп слабий син шлюхи котрий получає піздонів весь час',
'не бійся мене свинорус обриганий я ж лише тобі матір шлюху в рило виєбав',
'мовчи давай косоглазий синяра шлюхи я тобі рило рвав нахуй',
'береш мій хуй замість памперсу собі ару',
'антихрист твою русоблядську матір шлюху в сраку єбав во славу України',
'один хуй ти циган єбаний обожнюєш українські пеніси',
'нахуй ти сосеш мій хуй віслюк єбаний відірвись вже від нього',
'один хуй ти слабак котрий мого хуйця заглотне',
'русоблядь твою матір шлюху в рило хохли єбуть ',
'як тобі на смак український хуй син шалави',
'ти нахуй мені тут відсосав слабак блядський',
'циганку єбану трахаємо як не в себе хєхє',
'син шлюхози криволапий відсоси мені',
'ну і нахуй ти помер на хуї тут',
'ні нащо не здатний синяра шлюхи не помирай прям тут',
'один хуй слабак єбаний ти',
'твою маму хуями єбали',
'чого ти так бігаєш від мого хуя слабачок блядоруснявосвинотний я тобі тут кривозубу циганськоподібну матір шлюху поєбу',
'буду тебе принижувати поки остаточно не помреш від хуя',
'вічніть буду твою мати шлюху терирозувати своїм хуйом українським',
'нахуй ти тут свій відсос показав ару',
'не помирай син шалави руснявий я ж твої копита відпилю за таке',
'твою матір шлюху з балкону хуйом скинув ару',
'так та закрий нахуй своє чорне рило і відсоси мені тут',
'хуячим тебе синка блядорилої шиншили нахуй',
'ти чого вже відсосав єбаний блядорус',
'зніму з тебе шкіру син хуйні ти',
'і так і так відсосеш мій хуй',
'як би ти не старався все одно залишешся терпнем єбаним',
'все твоє життя в тебе харкати будемо синчело шалави котре відбилося від стада']
shabl1 = ["ᴛᥙ ᴦ᧐᧘᧐ᤋᥲдᥙᥔ ᥴᥙн ɯᥲ᧘ᥲʙᥙ ᤋᥲκρᥙᥔ ρᥙ᧘᧐ нᥲ᥊уᥔ ᥴʙ᧐є я ж ᴛ᧐δі ᴛуᴛ ᥴρᥲκу єδᥲʙ",
"ᥴ᧘ᥲδᥲκ δ᧘яд᧐ρуᥴняʙᥙᥔ я ᴛ᧐δі ᴛуᴛ ні ɯᥲнᥴу нᥱ ᤋᥲ᧘ᥙɯу нᥲ᥊уᥔ ",
"нᥱ ʙᥙ᥊ρюκуᥔ ᴛуᴛ ᥴᥙн ɯᥲ᧘ᥲʙᥙ κρᥙʙ᧐ρуκᥙᥔ",
"я ᴛ᧐δі ᴛуᴛ ⲙᥲᴛᥙ ɯ᧘ю᥊у єδᥲɯу ᴦ᧐᧘ᥙⲙᥙ ρуκᥲⲙᥙ ᥲρу",
"нᥲ᥊уᥔ ᴛᥙ ρуᥴняʙᥙᥔ ᥴᥙн ɯ᧘ю᥊ᥙ ᥰ᧐ⲙᥱρ ᴛуᴛ",
"ᥴʙᥙня δ᧘яд᧐ρᥙ᧘ᥲ я ᴛᥱδᥱ ᴛуᴛ нᥲ᥊уᥔ ʙ ж᧐ᥰу єδу",
"ᤋᥲʙᥲ᧘ᥙ єδᥲ᧘᧐ ᥴʙ᧐є ᥴʙᥙня κρᥙʙ᧐ᤋуδᥲ нᥲ᥊уᥔ і нᥱ ᥰᥙɯᥙ ᥴюдᥙ ʙᤋᥲᴦᥲ᧘і",
"ᴛᥙ ᴛρуᥴ᧘ᥙʙᥲ ᥴʙ᧐᧘᧐ᴛᥲ ρуᥴняʙ᧐ρᥙ᧘ᥲ я ᴛ᧐δі ᤋᥲρᥲᤋ ᴛʙ᧐є ᥴʙᥙннᥱ ρᥙ᧘᧐ ᥰᥱρᥱ᧘᧐ⲙᥲю",
"нᥱ ᥰ᧐ⲙᥙρᥲᥔ ᴛуᴛ ᥴ᧘ᥲδᥲκ єδᥲнᥙᥔ",
"нᥲ ᥊ую ᴛᥙ ʙідκᥙнуʙ κ᧐ᥰᥙᴛᥲ ρуᥴняʙі ᥲρу",
"яκᥙᥔ ᴛ᧐δі н᧐н ᥴᴛ᧐ᥰ ᥴ᧘ᥲδᥙᥔ ᥴᥙн ɯ᧘ю᥊ᥙ κ᧐ᴛρᥙᥔ ᥰ᧐᧘учᥲє ᥰіᤋд᧐ніʙ ʙᥱᥴь чᥲᥴ",
"нᥱ δіᥔᥴя ⲙᥱнᥱ ᥴʙᥙн᧐ρуᥴ ᧐δρᥙᴦᥲнᥙᥔ я ж ᧘ᥙɯᥱ ᴛ᧐δі ⲙᥲᴛіρ ɯ᧘ю᥊у ʙ ρᥙ᧘᧐ ʙᥙєδᥲʙ",
"ⲙ᧐ʙчᥙ дᥲʙᥲᥔ κ᧐ᥴ᧐ᴦ᧘ᥲᤋᥙᥔ ᥴᥙняρᥲ ɯ᧘ю᥊ᥙ я ᴛ᧐δі ρᥙ᧘᧐ ρʙᥲʙ нᥲ᥊уᥔ",
"δᥱρᥱɯ ⲙіᥔ ᥊уᥔ ᤋᥲⲙіᥴᴛь ᥰᥲⲙᥰᥱρᥴу ᥴ᧐δі ᥲρу",
"ᥲнᴛᥙ᥊ρᥙᥴᴛ ᴛʙ᧐ю ρуᥴ᧐δ᧘ядᥴьκу ⲙᥲᴛіρ ɯ᧘ю᥊у ʙ ᥴρᥲκу єδᥲʙ ʙ᧐ ᥴ᧘ᥲʙу Уκρᥲїнᥙ",
"᧐дᥙн ᥊уᥔ ᴛᥙ цᥙᴦᥲн єδᥲнᥙᥔ ᧐δ᧐жнюєɯ уκρᥲїнᥴьκі ᥰᥱніᥴᥙ",
"нᥲ᥊уᥔ ᴛᥙ ᥴ᧐ᥴᥱɯ ⲙіᥔ ᥊уᥔ ʙіᥴ᧘юκ єδᥲнᥙᥔ ʙідіρʙᥙᥴь ʙжᥱ ʙід нь᧐ᴦ᧐",
"᧐дᥙн ᥊уᥔ ᴛᥙ ᥴ᧘ᥲδᥲκ κ᧐ᴛρᥙᥔ ⲙ᧐ᴦ᧐ ᥊уᥔця ᤋᥲᴦ᧘᧐ᴛнᥱ",
"ρуᥴ᧐δ᧘ядь ᴛʙ᧐ю ⲙᥲᴛіρ ɯ᧘ю᥊у ʙ ρᥙ᧘᧐ ᥊᧐᥊᧘ᥙ єδуᴛь ",
"яκ ᴛ᧐δі нᥲ ᥴⲙᥲκ уκρᥲїнᥴьκᥙᥔ ᥊уᥔ ᥴᥙн ɯᥲ᧘ᥲʙᥙ",
"ᴛᥙ нᥲ᥊уᥔ ⲙᥱні ᴛуᴛ ʙідᥴ᧐ᥴᥲʙ ᥴ᧘ᥲδᥲκ δ᧘ядᥴьκᥙᥔ",
"цᥙᴦᥲнκу єδᥲну ᴛρᥲ᥊ᥲєⲙ᧐ яκ нᥱ ʙ ᥴᥱδᥱ ᥊є᥊є",
"ᥴᥙн ɯ᧘ю᥊᧐ᤋᥙ κρᥙʙ᧐᧘ᥲᥰᥙᥔ ʙідᥴ᧐ᥴᥙ ⲙᥱні",
"ну і нᥲ᥊уᥔ ᴛᥙ ᥰ᧐ⲙᥱρ нᥲ ᥊уї ᴛуᴛ",
"ні нᥲщ᧐ нᥱ ᤋдᥲᴛнᥙᥔ ᥴᥙняρᥲ ɯ᧘ю᥊ᥙ нᥱ ᥰ᧐ⲙᥙρᥲᥔ ᥰρяⲙ ᴛуᴛ",
"᧐дᥙн ᥊уᥔ ᥴ᧘ᥲδᥲκ єδᥲнᥙᥔ ᴛᥙ",
"ᴛʙ᧐ю ⲙᥲⲙу ᥊уяⲙᥙ єδᥲ᧘ᥙ",
"ч᧐ᴦ᧐ ᴛᥙ ᴛᥲκ δіᴦᥲєɯ ʙід ⲙ᧐ᴦ᧐ ᥊уя ᥴ᧘ᥲδᥲч᧐κ δ᧘яд᧐ρуᥴняʙ᧐ᥴʙᥙн᧐ᴛнᥙᥔ я ᴛ᧐δі ᴛуᴛ κρᥙʙ᧐ᤋуδу цᥙᴦᥲнᥴьκ᧐ᥰ᧐діδну ⲙᥲᴛіρ ɯ᧘ю᥊у ᥰ᧐єδу",
"δуду ᴛᥱδᥱ ᥰρᥙнᥙжуʙᥲᴛᥙ ᥰ᧐κᥙ ᧐ᥴᴛᥲᴛ᧐чн᧐ нᥱ ᥰ᧐ⲙρᥱɯ ʙід ᥊уя",
"ʙічніᴛь δуду ᴛʙ᧐ю ⲙᥲᴛᥙ ɯ᧘ю᥊у ᴛᥱρᥙρ᧐ᤋуʙᥲᴛᥙ ᥴʙ᧐їⲙ ᥊уᥔ᧐ⲙ уκρᥲїнᥴьκᥙⲙ",
"нᥲ᥊уᥔ ᴛᥙ ᴛуᴛ ᥴʙіᥔ ʙідᥴ᧐ᥴ ᥰ᧐κᥲᤋᥲʙ ᥲρу",
"нᥱ ᥰ᧐ⲙᥙρᥲᥔ ᥴᥙн ɯᥲ᧘ᥲʙᥙ ρуᥴняʙᥙᥔ я ж ᴛʙ᧐ї κ᧐ᥰᥙᴛᥲ ʙідᥰᥙ᧘ю ᤋᥲ ᴛᥲκᥱ",
"ᴛʙ᧐ю ⲙᥲᴛіρ ɯ᧘ю᥊у ᤋ δᥲ᧘κ᧐ну ᥊уᥔ᧐ⲙ ᥴκᥙнуʙ ᥲρу",
"ᴛᥲκ ᴛᥲ ᤋᥲκρᥙᥔ нᥲ᥊уᥔ ᥴʙ᧐є ч᧐ρнᥱ ρᥙ᧘᧐ і ʙідᥴ᧐ᥴᥙ ⲙᥱні ᴛуᴛ",
"᥊уячᥙⲙ ᴛᥱδᥱ ᥴᥙнκᥲ δ᧘яд᧐ρᥙ᧘᧐ї ɯᥙнɯᥙ᧘ᥙ нᥲ᥊уᥔ",
"ᴛᥙ ч᧐ᴦ᧐ ʙжᥱ ʙідᥴ᧐ᥴᥲʙ єδᥲнᥙᥔ δ᧘яд᧐ρуᥴ",
"ᤋніⲙу ᤋ ᴛᥱδᥱ ɯκіρу ᥴᥙн ᥊уᥔні ᴛᥙ",
"і ᴛᥲκ і ᴛᥲκ ʙідᥴ᧐ᥴᥱɯ ⲙіᥔ ᥊уᥔ",
"яκ δᥙ ᴛᥙ нᥱ ᥴᴛᥲρᥲʙᥴя ʙᥴᥱ ᧐дн᧐ ᤋᥲ᧘ᥙɯᥱɯᥴя ᴛᥱρᥰнᥱⲙ єδᥲнᥙⲙ",
"ʙᥴᥱ ᴛʙ᧐є жᥙᴛᴛя ʙ ᴛᥱδᥱ ᥊ᥲρκᥲᴛᥙ δудᥱⲙ᧐ ᥴᥙнчᥱ᧘᧐ ɯᥲ᧘ᥲʙᥙ κ᧐ᴛρᥱ ʙідδᥙ᧘᧐ᥴя ʙід ᥴᴛᥲдᥲ"]
shabl2 = ["ᴛи ᴦᴏᴧᴏɜᴀдий ᴄин ɯᴀᴧᴀʙи ɜᴀᴋᴩий ᴩиᴧᴏ нᴀхуй ᴄʙᴏє я ж ᴛᴏбі ᴛуᴛ ᴄᴩᴀᴋу єбᴀʙ",
"ᴄᴧᴀбᴀᴋ бᴧядᴏᴩуᴄняʙий я ᴛᴏбі ᴛуᴛ ні ɯᴀнᴄу нᴇ ɜᴀᴧиɯу нᴀхуй ",
"нᴇ ʙихᴩюᴋуй ᴛуᴛ ᴄин ɯᴀᴧᴀʙи ᴋᴩиʙᴏᴩуᴋий",
"я ᴛᴏбі ᴛуᴛ ʍᴀᴛи ɯᴧюху єбᴀɯу ᴦᴏᴧиʍи ᴩуᴋᴀʍи ᴀᴩу",
"нᴀхуй ᴛи ᴩуᴄняʙий ᴄин ɯᴧюхи ᴨᴏʍᴇᴩ ᴛуᴛ",
"ᴄʙиня бᴧядᴏᴩиᴧᴀ я ᴛᴇбᴇ ᴛуᴛ нᴀхуй ʙ жᴏᴨу єбу",
"ɜᴀʙᴀᴧи єбᴀᴧᴏ ᴄʙᴏє ᴄʙиня ᴋᴩиʙᴏɜубᴀ нᴀхуй і нᴇ ᴨиɯи ᴄюди ʙɜᴀᴦᴀᴧі",
"ᴛи ᴛᴩуᴄᴧиʙᴀ ᴄʙᴏᴧᴏᴛᴀ ᴩуᴄняʙᴏᴩиᴧᴀ я ᴛᴏбі ɜᴀᴩᴀɜ ᴛʙᴏє ᴄʙиннᴇ ᴩиᴧᴏ ᴨᴇᴩᴇᴧᴏʍᴀю",
"нᴇ ᴨᴏʍиᴩᴀй ᴛуᴛ ᴄᴧᴀбᴀᴋ єбᴀний",
"нᴀ хую ᴛи ʙідᴋинуʙ ᴋᴏᴨиᴛᴀ ᴩуᴄняʙі ᴀᴩу",
"яᴋий ᴛᴏбі нᴏн ᴄᴛᴏᴨ ᴄᴧᴀбий ᴄин ɯᴧюхи ᴋᴏᴛᴩий ᴨᴏᴧучᴀє ᴨіɜдᴏніʙ ʙᴇᴄь чᴀᴄ",
"нᴇ бійᴄя ʍᴇнᴇ ᴄʙинᴏᴩуᴄ ᴏбᴩиᴦᴀний я ж ᴧиɯᴇ ᴛᴏбі ʍᴀᴛіᴩ ɯᴧюху ʙ ᴩиᴧᴏ ʙиєбᴀʙ",
"ʍᴏʙчи дᴀʙᴀй ᴋᴏᴄᴏᴦᴧᴀɜий ᴄиняᴩᴀ ɯᴧюхи я ᴛᴏбі ᴩиᴧᴏ ᴩʙᴀʙ нᴀхуй",
"бᴇᴩᴇɯ ʍій хуй ɜᴀʍіᴄᴛь ᴨᴀʍᴨᴇᴩᴄу ᴄᴏбі ᴀᴩу",
"ᴀнᴛихᴩиᴄᴛ ᴛʙᴏю ᴩуᴄᴏбᴧядᴄьᴋу ʍᴀᴛіᴩ ɯᴧюху ʙ ᴄᴩᴀᴋу єбᴀʙ ʙᴏ ᴄᴧᴀʙу Ꭹᴋᴩᴀїни",
"ᴏдин хуй ᴛи циᴦᴀн єбᴀний ᴏбᴏжнюєɯ уᴋᴩᴀїнᴄьᴋі ᴨᴇніᴄи",
"нᴀхуй ᴛи ᴄᴏᴄᴇɯ ʍій хуй ʙіᴄᴧюᴋ єбᴀний ʙідіᴩʙиᴄь ʙжᴇ ʙід ньᴏᴦᴏ",
"ᴏдин хуй ᴛи ᴄᴧᴀбᴀᴋ ᴋᴏᴛᴩий ʍᴏᴦᴏ хуйця ɜᴀᴦᴧᴏᴛнᴇ",
"ᴩуᴄᴏбᴧядь ᴛʙᴏю ʍᴀᴛіᴩ ɯᴧюху ʙ ᴩиᴧᴏ хᴏхᴧи єбуᴛь ",
"яᴋ ᴛᴏбі нᴀ ᴄʍᴀᴋ уᴋᴩᴀїнᴄьᴋий хуй ᴄин ɯᴀᴧᴀʙи",
"ᴛи нᴀхуй ʍᴇні ᴛуᴛ ʙідᴄᴏᴄᴀʙ ᴄᴧᴀбᴀᴋ бᴧядᴄьᴋий",
"циᴦᴀнᴋу єбᴀну ᴛᴩᴀхᴀєʍᴏ яᴋ нᴇ ʙ ᴄᴇбᴇ хєхє",
"ᴄин ɯᴧюхᴏɜи ᴋᴩиʙᴏᴧᴀᴨий ʙідᴄᴏᴄи ʍᴇні",
"ну і нᴀхуй ᴛи ᴨᴏʍᴇᴩ нᴀ хуї ᴛуᴛ",
"ні нᴀщᴏ нᴇ ɜдᴀᴛний ᴄиняᴩᴀ ɯᴧюхи нᴇ ᴨᴏʍиᴩᴀй ᴨᴩяʍ ᴛуᴛ",
"ᴏдин хуй ᴄᴧᴀбᴀᴋ єбᴀний ᴛи",
"ᴛʙᴏю ʍᴀʍу хуяʍи єбᴀᴧи",
"чᴏᴦᴏ ᴛи ᴛᴀᴋ біᴦᴀєɯ ʙід ʍᴏᴦᴏ хуя ᴄᴧᴀбᴀчᴏᴋ бᴧядᴏᴩуᴄняʙᴏᴄʙинᴏᴛний я ᴛᴏбі ᴛуᴛ ᴋᴩиʙᴏɜубу циᴦᴀнᴄьᴋᴏᴨᴏдібну ʍᴀᴛіᴩ ɯᴧюху ᴨᴏєбу",
"буду ᴛᴇбᴇ ᴨᴩинижуʙᴀᴛи ᴨᴏᴋи ᴏᴄᴛᴀᴛᴏчнᴏ нᴇ ᴨᴏʍᴩᴇɯ ʙід хуя",
"ʙічніᴛь буду ᴛʙᴏю ʍᴀᴛи ɯᴧюху ᴛᴇᴩиᴩᴏɜуʙᴀᴛи ᴄʙᴏїʍ хуйᴏʍ уᴋᴩᴀїнᴄьᴋиʍ",
"нᴀхуй ᴛи ᴛуᴛ ᴄʙій ʙідᴄᴏᴄ ᴨᴏᴋᴀɜᴀʙ ᴀᴩу",
"нᴇ ᴨᴏʍиᴩᴀй ᴄин ɯᴀᴧᴀʙи ᴩуᴄняʙий я ж ᴛʙᴏї ᴋᴏᴨиᴛᴀ ʙідᴨиᴧю ɜᴀ ᴛᴀᴋᴇ",
"ᴛʙᴏю ʍᴀᴛіᴩ ɯᴧюху ɜ бᴀᴧᴋᴏну хуйᴏʍ ᴄᴋинуʙ ᴀᴩу",
"ᴛᴀᴋ ᴛᴀ ɜᴀᴋᴩий нᴀхуй ᴄʙᴏє чᴏᴩнᴇ ᴩиᴧᴏ і ʙідᴄᴏᴄи ʍᴇні ᴛуᴛ",
"хуячиʍ ᴛᴇбᴇ ᴄинᴋᴀ бᴧядᴏᴩиᴧᴏї ɯинɯиᴧи нᴀхуй",
"ᴛи чᴏᴦᴏ ʙжᴇ ʙідᴄᴏᴄᴀʙ єбᴀний бᴧядᴏᴩуᴄ",
"ɜніʍу ɜ ᴛᴇбᴇ ɯᴋіᴩу ᴄин хуйні ᴛи",
"і ᴛᴀᴋ і ᴛᴀᴋ ʙідᴄᴏᴄᴇɯ ʍій хуй",
"яᴋ би ᴛи нᴇ ᴄᴛᴀᴩᴀʙᴄя ʙᴄᴇ ᴏднᴏ ɜᴀᴧиɯᴇɯᴄя ᴛᴇᴩᴨнᴇʍ єбᴀниʍ",
"ʙᴄᴇ ᴛʙᴏє жиᴛᴛя ʙ ᴛᴇбᴇ хᴀᴩᴋᴀᴛи будᴇʍᴏ ᴄинчᴇᴧᴏ ɯᴀᴧᴀʙи ᴋᴏᴛᴩᴇ ʙідбиᴧᴏᴄя ʙід ᴄᴛᴀдᴀ"]
state = True
state1 = True
state2 = True
state3 = True
state4 = True
state5 = True
start = datetime.now()
time = 30
time1 = 30
time2 = 30
ph = "https://x0.at/q73-.mp4"
ph1 = "https://x0.at/ENii.mp4"
ph2 = "https://x0.at/abS_.mp4"
menu = "https://x0.at/7awl.mp4"
uptime = "https://x0.at/bF65.mp4"
mediaid = "https://x0.at/nzYA.mp4"
custom = "https://x0.at/hxAt.mp4"
start1 = 'https://x0.at/ENii.mp4'
shapka = "興 ᴨᴏчуʙᴀюᴄя ᴋᴩᴀщᴇ ᴄᴇᴩᴇд ᴨᴏʍᴇᴩᴧих ᴋᴏᴩᴏᴧіʙ ♯"
shapka1 = "興 ᴨᴏчуʙᴀюᴄя ᴋᴩᴀщᴇ ᴄᴇᴩᴇд ᴨᴏʍᴇᴩᴧих ᴋᴏᴩᴏᴧіʙ ♯"
shapka2 = "興 ᴨᴏчуʙᴀюᴄя ᴋᴩᴀщᴇ ᴄᴇᴩᴇд ᴨᴏʍᴇᴩᴧих ᴋᴏᴩᴏᴧіʙ ♯"
name = "ᎳᎪᏒᏒᎬN ᎳᎪᏒᏒᏆᏫᏒ ᏴᏫᎢ"
media_file = ""
admin_id = "5836993624"
adminchange = "5836993624"

class PydroidBot:
    def __init__(self):
        self.api_id = 26736366
        self.api_hash = "10a653547ac17ab466a92238755ffcec"
        self.client = TelegramClient('main', self.api_id, self.api_hash)
        self.client.start()


        @self.client.on(events.NewMessage(pattern='/uptime'))
        async def command_help_commands(event):
            if str(event.message.sender_id) == admin_id:
                time_now = datetime.now()
                timing = time_now - start
                time_string = str(timing)
                time_result = time_string.split(".")[0]
                chat_id = event.chat_id
                me = await self.client.get_me()
                await self.client.send_file(chat_id, uptime, caption='ᏌᏢᎢᏆᎷᎬ: <code>{}</code>'.format(time_result), parse_mode='html')

    def run(self):
        @self.client.on(events.NewMessage(pattern=r'\/terror'))
        async def command_fast(event):
            user_id = event.message.sender_id
            if str(user_id) == admin_id:
                txt = event.message.message.split(maxsplit=1)[1]
                chat_id = int(txt)
                await event.respond("<b>ᥴᥰᥲⲙ ᴛᥱκᥴᴛ᧐ⲙ ʙʙіⲙκнᥱн᧐!</b>\nщ᧐δ ʙᥙⲙκнуᴛᥙ ᥰᥙɯᥙ <code>/stop 1</code>", parse_mode='html')
                global state
                state = True
                while state:
                    text = ch(shabl)
                    await self.client.send_message(chat_id, shapka+text)
                    await sl(int(time))

        @self.client.on(events.NewMessage(pattern=r'\/mterror'))
        async def command_fastph(event):
            user_id = event.message.sender_id
            txt = event.message.message.split(maxsplit=1)[1]
            if str(user_id) == admin_id:
                chat_id = int(txt)
                await event.respond("<b>ᥴᥰᥲⲙ ᤋ ⲙᥱдіᥲ ʙʙіⲙκнᥱн᧐!</b>\nщ᧐δ ʙᥙⲙκнуᴛᥙ ᥰᥙɯᥙ <code>/stop 2</code>", parse_mode='html')
                global state1
                state1 = True
                while state1:
                    text = ch(shabl)
                    await self.client.send_file(chat_id, ph, caption=shapka+text)
                    await sl(int(time))

        @self.client.on(events.NewMessage(pattern='/time'))
        async def command_set_time(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global time
                time = int(text)
                await event.respond("<b>ᤋᥲᴛρᥙⲙκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/media'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global ph
                ph = text
                await event.respond("<b>ⲙᥱдіᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/text'))
        async def command_set_shapka(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global shapka
                shapka = str(text)
                await event.respond('<b>ɯᥲᥰκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>', parse_mode='html')


        @self.client.on(events.NewMessage(pattern='/stop'))
        async def command_stop(event):
            global state, state1, state2, state3
            stop_number = event.message.message.split(maxsplit=1)[1]
            if str(event.message.sender_id) == admin_id:
                if stop_number == "1":
                    state = False
                    await event.respond("<b>ᥴᥰᥲⲙ ᴛᥱκᥴᴛ᧐ⲙ ᤋуᥰᥙнᥱн᧐!</b>", parse_mode='html')
                if stop_number == "2":
                    state1 = False
                    await event.respond("<b>ᥴᥰᥲⲙ ᤋ ⲙᥱдіᥲ ᤋуᥰᥙнᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/menu'))
        async def command_help_commands(event):
            if str(event.message.sender_id) == admin_id:
                chat_id = event.chat_id
                me = await self.client.get_me()
                await self.client.send_file(chat_id, menu, caption='<b>'+name+'</b>''\n\n✙ команди для першого режиму спаму:\nꏢ <code>/terror</code> + chat id — спам текстом\nꏢ <code>/mterror</code> + chat id — спам медіа\nꏢ <code>/time</code> + time — затримка для спама\nꏢ <code>/media</code> + link — медіа для спама\nꏢ <code>/text</code> + text — шапка для спама\nꏢ <code>/stop</code> + number — закінчення спаму [1 - text], [2 - media]\n\n✙ команди для другого режиму спаму:\nꏢ <code>/nterror</code> + chat id — спам текстом\nꏢ <code>/nmterror</code> + chat id — спам медіа\nꏢ <code>/ntime</code> + time — затримка для спама\nꏢ <code>/nmedia</code> + link — медіа для спама\nꏢ <code>/ntext</code> + text — шапка для спама\nꏢ <code>/nstop</code> + number — закінчення спаму [1 - text], [2 - media]\n\n✙ команди для третього режиму спаму:\nꏢ <code>/qterror</code> + chat id — спам текстом\nꏢ <code>/qmterror</code> + chat id — спам медіа\nꏢ <code>/qtime</code> + time — затримка для спама\nꏢ <code>/qmedia</code> + link — медіа для спама\nꏢ <code>/qtext</code> + text — шапка для спама\nꏢ <code>/qstop</code> + number — закінчення спаму [1 - text], [2 - media]\n\n♯ інші команди — /start\n\n⛨ chat id: <code>{}</code>\n⛨ user id: <code>{}</code>\n⛨ nickname: <code>{}</code>\n⛨ username: <b>@{}</b>'.format(chat_id, me.id, me.first_name, me.username), parse_mode='html')


        @self.client.on(events.NewMessage(pattern='/id'))
        async def command_help_commands(event):
            if str(event.message.sender_id) == admin_id:
                chat_id = event.chat_id
                me = await self.client.get_me()
                await self.client.send_file(chat_id, mediaid, caption='<b>ᏟᎻᎪᎢ ᏆᎠ:</b> <code>{}</code>'.format(chat_id), parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/start'))
        async def command_help_commands(event):
            if str(event.message.sender_id) == admin_id:
                chat_id = event.chat_id
                me = await self.client.get_me()
                await self.client.send_file(chat_id, start1, caption='вітаю з покупкою бота!\n<b>⛧'+name+'⛧</b>\nкоманди для користування ботом:\n\n⛧ <code>/menu</code> - дізнатись всі команди бота\n⛧ <code>/id</code> - дізнатись айді чату\n⛧ <code>/uptime</code> - дізнатись час роботи бота\n⛧ <code>/start</code> - викликати це меню\n⛧ <code>/custom</code> - дізнатись команди для зміни виду бота\n\n\n♱ розробник бота: <b>@NalledWarren</b>'.format(), parse_mode='html')

        @self.client.on(events.NewMessage(pattern=r'\/nterror'))
        async def command_fast(event):
            user_id = event.message.sender_id
            if str(user_id) == admin_id:
                txt = event.message.message.split(maxsplit=1)[1]
                chat_id = int(txt)
                await event.respond("<b>ᥴᥰᥲⲙ ᴛᥱκᥴᴛ᧐ⲙ ʙʙіⲙκнᥱн᧐!</b>\nщ᧐δ ʙᥙⲙκнуᴛᥙ ᥰᥙɯᥙ <code>/nstop 1</code>", parse_mode='html')
                global state2
                state2 = True
                while state2:
                    text = ch(shabl1)
                    await self.client.send_message(chat_id, shapka1+text)
                    await sl(int(time1))

        @self.client.on(events.NewMessage(pattern=r'\/nmterror'))
        async def command_fastph(event):
            user_id = event.message.sender_id
            txt = event.message.message.split(maxsplit=1)[1]
            if str(user_id) == admin_id:
                chat_id = int(txt)
                await event.respond("<b>ᥴᥰᥲⲙ ᤋ ⲙᥱдіᥲ ʙʙіⲙκнᥱн᧐!</b>\nщ᧐δ ʙᥙⲙκнуᴛᥙ ᥰᥙɯᥙ <code>/nstop 2</code>", parse_mode='html')
                global state3
                state3 = True
                while state3:
                    text = ch(shabl1)
                    await self.client.send_file(chat_id, ph1, caption=shapka1+text)
                    await sl(int(time1))

        @self.client.on(events.NewMessage(pattern='/ntime'))

        async def command_set_time(event):

            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global time1
                time1 = int(text)
                await event.respond("<b>ᤋᥲᴛρᥙⲙκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/nmedia'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global ph1
                ph1 = text
                await event.respond("<b>ⲙᥱдіᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/ntext'))
        async def command_set_shapka(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global shapka1
                shapka1 = str(text)
                await event.respond('<b>ɯᥲᥰκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>', parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/nstop'))

        async def command_stop(event):

            global state2, state3
            stop_number = event.message.message.split(maxsplit=1)[1]
            if str(event.message.sender_id) == admin_id:
                if stop_number == "1":
                    state2 = False
                    await event.respond("<b>ᥴᥰᥲⲙ ᴛᥱκᥴᴛ᧐ⲙ ᤋуᥰᥙнᥱн᧐!</b>", parse_mode='html')
                if stop_number == "2":
                    state3 = False
                    await event.respond("<b>ᥴᥰᥲⲙ ᤋ ⲙᥱдіᥲ ᤋуᥰᥙнᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern=r'\/qterror'))
        async def command_fast(event):
            user_id = event.message.sender_id
            if str(user_id) == admin_id:
                txt = event.message.message.split(maxsplit=1)[1]
                chat_id = int(txt)
                await event.respond("<b>ᥴᥰᥲⲙ ᴛᥱκᥴᴛ᧐ⲙ ʙʙіⲙκнᥱн᧐!</b>\nщ᧐δ ʙᥙⲙκнуᴛᥙ ᥰᥙɯᥙ <code>/qstop 1</code>", parse_mode='html')
                global state4
                state4 = True
                while state4:
                    text = ch(shabl2)
                    await self.client.send_message(chat_id, shapka2+text)
                    await sl(int(time2))

        @self.client.on(events.NewMessage(pattern=r'\/qmterror'))
        async def command_fastph(event):
            user_id = event.message.sender_id
            txt = event.message.message.split(maxsplit=1)[1]
            if str(user_id) == admin_id:
                chat_id = int(txt)
                await event.respond("<b>ᥴᥰᥲⲙ ᤋ ⲙᥱдіᥲ ʙʙіⲙκнᥱн᧐!</b>\nщ᧐δ ʙᥙⲙκнуᴛᥙ ᥰᥙɯᥙ <code>/qstop 2</code>", parse_mode='html')
                global state5
                state5 = True
                while state5:
                    text = ch(shabl2)
                    await self.client.send_file(chat_id, ph2, caption=shapka2+text)
                    await sl(int(time2))

        @self.client.on(events.NewMessage(pattern='/qtime'))

        async def command_set_time(event):

            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global time2
                time2 = int(text)
                await event.respond("<b>ᤋᥲᴛρᥙⲙκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/qmedia'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global ph2
                ph2 = text
                await event.respond("<b>ⲙᥱдіᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/qtext'))
        async def command_set_shapka(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global shapka2
                shapka2 = str(text)
                await event.respond('<b>ɯᥲᥰκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>', parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/qstop'))
        async def command_stop(event):
            global state4, state5
            stop_number = event.message.message.split(maxsplit=1)[1]
            if str(event.message.sender_id) == admin_id:
                if stop_number == "1":
                    state4 = False
                    await event.respond("<b>ᥴᥰᥲⲙ ᴛᥱκᥴᴛ᧐ⲙ ᤋуᥰᥙнᥱн᧐!</b>", parse_mode='html')
                if stop_number == "2":
                    state5 = False
                    await event.respond("<b>ᥴᥰᥲⲙ ᤋ ⲙᥱдіᥲ ᤋуᥰᥙнᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/name'))
        async def command_set_shapka(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global name
                name = str(text)
                await event.respond('<b>нᥲᤋʙᥲ δ᧐ᴛᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>', parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/muptime'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global uptime
                uptime = text
                await event.respond("<b>ⲙᥱдіᥲ д᧘я ᥲᥰᴛᥲᥔⲙᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/mmenu'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global menu
                menu = text
                await event.respond("<b>ⲙᥱдіᥲ д᧘я ⲙᥱню ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/mid'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global mediaid
                mediaid = text
                await event.respond("<b>ⲙᥱдіᥲ д᧘я ᥲᥔді ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/custom'))
        async def command_help_commands(event):
            if str(event.message.sender_id) == admin_id:
                chat_id = event.chat_id
                me = await self.client.get_me()
                await self.client.send_file(chat_id, custom, caption='<b>custom in '+name+'</b>\n\n興 <code>/name</code> + text — change bot name\n興 <code>/mmenu</code> + link —  change media [ /menu ]\n興 <code>/mid</code> + link — change media [ /id ]\n興 <code>/muptime</code> + link — change media [ /uptime ]\n興 <code>/mcustom</code> + link — change media [ /custom ]\n興 <code>/mstart</code> + link — change media [ /start ]'.format(), parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/mcustom'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global custom
                custom = text
                await event.respond("<b>ⲙᥱдіᥲ д᧘я κᥲᥴᴛ᧐ⲙκᥙ ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/mstart'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global start1
                start1 = text
                await event.respond("<b>ⲙᥱдіᥲ д᧘я ᥴᴛᥲρᴛу ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/admin'))
        async def command_set_shapka(event):
                text = event.message.message.split(maxsplit=1)[1]
                global admin_id
                admin_id = str(text)
                await event.respond('<b>✓</b>', parse_mode='html')


    def start(self):
        self.client.run_until_disconnected()

if __name__ == "__main__":
    start_class = PydroidBot()
    start_class.run()
    start_class.start()