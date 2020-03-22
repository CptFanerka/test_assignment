import quest_storage


quest_stages = dict()


quest_begin = quest_storage.QuestStage()
quest_begin.code = 'quest_begin'
quest_begin.name = 'Введение'
quest_begin.body = 'Вы - недовольный работодатель, желающий не принять на работу следующего соискателя. К вашей ' \
                   'радости, вот-вот как раз должна прийти некая Ксения, начинающий программист с амбициями и ' \
                   'желанием учиться новому:'
quest_begin.cases = ['quest_do_not_interview', 'quest_right_hand', 'quest_personal_interview']
quest_stages[quest_begin.code] = quest_begin


quest_do_not_interview = quest_storage.QuestStage()
quest_do_not_interview.code = 'quest_do_not_interview'
quest_do_not_interview.name = 'Не проводить собеседование'
quest_do_not_interview.body = 'Ксения приходит, но, не встретив никого, кто собирался бы провести с ней ' \
                              'собеседование, проходит к другим программистам и начинает работать с ними, полагая,' \
                              ' что уже назначена на должность. Вы не замечаете её несколько лет, а, наконец увидев,' \
                              ' понимаете, как неловко было бы прогонять её теперь.'
quest_do_not_interview.cases = ['quest_final']
quest_stages[quest_do_not_interview.code] = quest_do_not_interview


quest_right_hand = quest_storage.QuestStage()
quest_right_hand.code = 'quest_right_hand'
quest_right_hand.name = 'Доверить всё своей правой руке'
quest_right_hand.body = 'Вы вызываете в кабинет свою правую руку. Дождавшись подручного, вы раздумываете об указаниях' \
                        ' к собеседованию, прерывая размышления невольно вырывающимся злодейским хохотом:'
quest_right_hand.cases = ['quest_ignorance', 'quest_knowledge', 'quest_unsocial']
quest_stages[quest_right_hand.code] = quest_right_hand


quest_personal_interview = quest_storage.QuestStage()
quest_personal_interview.code = 'quest_personal_interview'
quest_personal_interview.name = 'Лично провести собеседование'
quest_personal_interview.body = 'Ксения заходит к вам в кабинет.'
quest_personal_interview.cases = ['quest_welcome', 'quest_examination', 'quest_animal']
quest_stages[quest_personal_interview.code] = quest_personal_interview


quest_ignorance = quest_storage.QuestStage()
quest_ignorance.code = 'quest_ignorance'
quest_ignorance.name = 'Отказывать при любых признаках незнания чего-либо'
quest_ignorance.body = 'Спустя полчаса к вам возвращается кадровик, сообщая, что Ксения знает обо всём, ' \
                       'что он спрашивает. Как выяснилось, на протяжении всего собеседования он повторял ' \
                       'единственный придуманный им вопрос: “Вы умеете программировать?”'
quest_ignorance.cases = ['quest_final']
quest_stages[quest_ignorance.code] = quest_ignorance


quest_knowledge = quest_storage.QuestStage()
quest_knowledge.code = 'quest_knowledge'
quest_knowledge.name = 'Отказывать при любых признаках знания чего-либо'
quest_knowledge.body = 'Спустя 5 минут кадровик возвращается, сообщив, что Ксения не знает ровным счетом ничего. ' \
                       'К сожалению, он забыл, что работает в IT компании, и провёл экзамен по креольскому языку.'
quest_knowledge.cases = ['quest_final']
quest_stages[quest_knowledge.code] = quest_knowledge


quest_unsocial = quest_storage.QuestStage()
quest_unsocial.code = 'quest_unsocial'
quest_unsocial.name = 'Отказывать, если соискатель не сможет поладить с коллективом'
quest_unsocial.body = 'Вернувшись на следующий день, кадровик докладывает, что во время собеседования разговорился ' \
                      'с Ксенией на посторонние темы, и, спустя время, они поехали домой, где всю ночь играли в ' \
                      'приставку, дрались подушками и смотрели американские комедии начала 2000-х, из-за чего он ' \
                      'совершенно позабыл, какие указания были даны.'
quest_unsocial.cases = ['quest_final']
quest_stages[quest_unsocial.code] = quest_unsocial


quest_welcome = quest_storage.QuestStage()
quest_welcome.code = 'quest_welcome'
quest_welcome.name = 'Добрый день, Ксения!'
quest_welcome.body = '- До.. д... добр... добро пожаловать на работу, Ксения! - ' \
                     'Вы сами не понимаете как вышла подобная оговорка, но слово не воробей, вылетит - не поймаешь...'
quest_welcome.cases = ['quest_final']
quest_stages[quest_welcome.code] = quest_welcome


quest_examination = quest_storage.QuestStage()
quest_examination.code = 'quest_examination'
quest_examination.name = 'Провести дотошный допрос о навыках, которыми она владеет'
quest_examination.body = 'Увы, но навыки Ксении оказываются на слишком подходящем уровне – знает достаточно, ' \
                         'чтобы работать, но слишком мало, чтобы быть раздражающей всезнайкой.'
quest_examination.cases = ['quest_next']
quest_stages[quest_examination.code] = quest_examination


quest_animal = quest_storage.QuestStage()
quest_animal.code = 'quest_animal'
quest_animal.name = 'Спросить, каким животным она хотела бы быть'
quest_animal.body = '- Плюшевой акулой, - без раздумий отвечает она. ' \
                    'Амбициозно, но достаточно безопасно. Вы не можете найти повода для отказа.'
quest_animal.cases = ['quest_next']
quest_stages[quest_animal.code] = quest_animal


quest_next = quest_storage.QuestStage()
quest_next.code = 'quest_next'
quest_next.name = 'Дальше'
quest_next.body = 'И вот вы уже вытаскиваете трудовой договор на стол, остался последний шанс отказать...'
quest_next.cases = ['quest_cross_out', 'quest_let_fly', 'quest_tear']
quest_stages[quest_next.code] = quest_next


quest_cross_out = quest_storage.QuestStage()
quest_cross_out.code = 'quest_cross_out'
quest_cross_out.name = 'Перечеркнуть договор'
quest_cross_out.body = 'Вы начинаете яростно чиркать по бумаге, не желая оставить ни кусочка чистой бумаги. ' \
                       'Когда пелена рассеивается, вы обнаруживаете, что перечёркивания слишком похожи на буквы ' \
                       'и подписи в нужных местах, а Ксения, даже не заметившая вашего покушения, расписывается в ' \
                       'нужном ей месте, спрашивая, когда выходить на работу.'
quest_cross_out.cases = ['quest_final']
quest_stages[quest_cross_out.code] = quest_cross_out


quest_let_fly = quest_storage.QuestStage()
quest_let_fly.code = 'quest_let_fly'
quest_let_fly.name = 'Выбросить договор в окно'
quest_let_fly.body = 'Вы бросаете договор в окно, лишая девушку уже почти полученной должности. Тишина. ' \
                     'Вы с довольным видом смотрите на ошарашенную Ксению, радуясь, что план все-таки удался. ' \
                     'Но неожиданно в кабинет входит кадровик с заполненным трудовым договором, и отдает его ' \
                     'будущей сотруднице на роспись. Урок на будущее: не выбрасывать трудовые договоры на вышедших ' \
                     'покурить кадровиков, они привыкли заполнять все увиденные документы не глядя.'
quest_let_fly.cases = ['quest_final']
quest_stages[quest_let_fly.code] = quest_let_fly


quest_tear = quest_storage.QuestStage()
quest_tear.code = 'quest_tear'
quest_tear.name = 'Разорвать договор'
quest_tear.body = 'Вы рвёте договор на маленькие кусочки, разбрасывая их по кабинету. Кажется, теперь у ' \
                  'Ксении не осталось никаких шансов. Продолжая бегать и раскидывать ошмётки, вы случайно ' \
                  'наступаете на пульт от телевизора, оставленный на полу. Включается новостная передача, ' \
                  'в которой сообщается, что с этого момента одним из способов заключения договоров официально ' \
                  'признано их разрывание и разбрасывание по комнате со второй стороной сделки. Ксения издает ' \
                  'облегчённый вздох, и, обрадовавшись, что её новый начальник с такой внимательностью следит ' \
                  'за последними новостями, отправляется на работу.'
quest_tear.cases = ['quest_final']
quest_stages[quest_tear.code] = quest_tear


quest_final = quest_storage.QuestStage()
quest_final.code = 'quest_final'
quest_final.name = 'ФИНАЛ'
quest_final.body = 'КСЕНИЯ ПРИНЯТА НА РАБОТУ'
quest_final.cases = []
quest_stages[quest_final.code] = quest_final


quest_storage.FileStorage.save([quest_begin, quest_do_not_interview, quest_right_hand, quest_personal_interview,
                                quest_ignorance, quest_knowledge, quest_unsocial, quest_welcome, quest_examination,
                                quest_animal, quest_next, quest_cross_out, quest_let_fly, quest_tear, quest_final])
quest_storage.FileStorage.load()