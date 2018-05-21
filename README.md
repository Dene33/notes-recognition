<h1>Recognition of music sheet and transcribing it into MIDI</h1>

<p><img alt="" src="https://i.imgur.com/4my6Ar7.gif" style="height:60px; width:344px" /></p>

<h3><strong>Подход к распознаванию нот</strong></h3>

<p>После определённого количества безуспешных&nbsp;попыток написания проекта&nbsp;с нуля и проверки разных подходов, наткнулся на следующую <a href="https://ismir2017.smcnus.org/wp-content/uploads/2017/10/34_Paper.pdf">статью</a>:&nbsp; В ней описан подход к распознаванию нот с помощью связки&nbsp;Convolutional и&nbsp;Recurrent сетей. Этот подход используется, в частности, для распознавания текста. Поэтому я решил взять одну из реализаций Optical Character Recognition и обучить сеть на базе нот.&nbsp;</p>

<p>Была выбрана <a href="https://github.com/emedvedev/attention-ocr">эта tensorflow модель</a>. <a href="https://arxiv.org/pdf/1609.04938v1.pdf">Научная статья</a>, объясняющая принцип её работы.&nbsp;</p>

<h3><strong>Датасет</strong></h3>

<p>Наиболее полная информация&nbsp;касательно датасетов по распознаванию нот находится <a href="https://github.com/apacha/OMR-Datasets">здесь.</a>&nbsp;Однако, датасетов с размеченной высотой нот, подходящих для моих задач не нашлось. Единственный доступный датасет со звуковысотным маппингом был взят <a href="https://www.dropbox.com/sh/ska6xvll07aeq0x/AADE6vm1etMCt-QuGCH78yP8a?dl=0">отсюда</a>, у ребят написавших оригинальную статью, ссылка на которую представлена выше.&nbsp;Он представляет из себя сгенерированные в <a href="http://lilypond.org/">Lilypond</a>&nbsp;изображения с соответствующими лейблами для каждой ноты и знака.</p>

<h3><strong>Характеристики&nbsp;датасета</strong></h3>

<p>94,984 случайных монофонических последовательностей, состоящих из 52 символов:&nbsp;музыкальных нот от С4 до Е5, 4 длительности (половина, четверь, восьмая, шестнадцатая), 4 паузы тех же длительностей, символы размеров&nbsp;(3/4, 4/4,&nbsp;6/8), знаки альтерации (диез, бемоль, бекар), скрипичный ключ, тактовая черта.</p>

<p>Поскольку датасет составлен из сгенерированных изображений, распознавание не будет адекватно&nbsp;работать с фотографиями. Также, с нотами, чья структура отличается от характеристик датасета.</p>

<p>Датасет был обработан, чтобы соответстовать требованиям сети для обучения (созданы лейблы, изображения уменьшены и т.д.). 95% - обучающая выборка 5% - тестовая.&nbsp;</p>

<h3><strong>Обучение</strong></h3>

<p>Сеть обучалась в течение около 8 часов на&nbsp;&nbsp;NVIDIA Tesla K80. 16 эпох.&nbsp;</p>

<h3><strong>Сложности</strong></h3>

<p>1. Сейчас модель может распознавать небольшие последовательности. Ей нельзя скормить весь лист с нотами. Однако, эта проблема решаема.&nbsp;Я пытался сделать сегментацию листа (вычленение тактов)&nbsp;силами OpenCV и добился определённых результатов. Но код&nbsp;очень по-разному работает для изображений разного качества. Поэтому, в долгосрочной перспективе,&nbsp;тут нужно тренировать отдельный слой сети.&nbsp;Для этого нужны данные с разметкой тактов, систем и прочих высокоуровневых&nbsp;элементов системы нотного листа.</p>

<p>2. Не успел сделать конвертацию в MIDI. К сожалению, вопрос в лоб не решить. Думал просто конвертировать обратно в Lilypond но сделать это оказалось не так легко из-за того, что программа сама проставляет знаки альтерации в зависимости от тональности и ещё пары тонкостей. Возможно, тут лучше подойдёт OpenXML, на изучение формата которого, однако, у меня не хватило времени.</p>

<p>3. Также не хватило времени&nbsp;на &quot;выкат в продакшен&quot; версии для удобного тестирования без каких-либо установок. Поэтому, чтобы поиграться с распознаванием, нужно поставить&nbsp;https://github.com/emedvedev/attention-ocr и запустить функцию тестирования, это опишу ниже.</p>

<p>4. Также не успел, как следует протестить и собрать статистику. Единичный&nbsp;прогон по тестовой выборке показал результат в 99,5%.&nbsp;</p>

<h3><strong>Как запустить</strong></h3>

<p>Устанавливаем&nbsp;<a href="https://www.tensorflow.org/install/">https://www.tensorflow.org/install/</a></p>

<p>Устанавливаем&nbsp;<a href="https://github.com/emedvedev/attention-ocr">https://github.com/emedvedev/attention-ocr</a></p>

<p>Качаем тестовую&nbsp;выборку:<a href="https://github.com/Dene33/notes-recognition/blob/master/notesTest.tfrecords?raw=true">&nbsp;https://github.com/Dene33/notes-recognition/blob/master/notesTest.tfrecords?raw=true</a></p>

<p>Качаем чекпоинты (это и есть обученная модель)&nbsp;и распаковываем:&nbsp;<a href="https://github.com/Dene33/notes-recognition/blob/master/checkpoints.zip">https://github.com/Dene33/notes-recognition/blob/master/checkpoints.zip?raw=true</a></p>

<p>Запускаем:&nbsp;</p>

<blockquote>
<p>aocr test --visualize ПУТЬ/К/notesTest.tfrecords --log-path ./log/log.log --max-width 1000 --max-height 61 --max-prediction 36 --full-ascii&nbsp;--model-dir ПУТЬ/К/checkpoints</p>
</blockquote>

<p>Наблюдаем за процессом. А потом смотрим на результат в папке log. Там будут находиться папки для каждой картинки, для которой было проведено распознавание. В каждой папке файл word.txt где первая строка - предсказанный результат, вторая - ground-truth Также в папке находится гифка, показывающая процесс работы нейросети.</p>

<p>Для перевода результат в читаемый формат (переименование папок и файлов), кидаем <a href="https://raw.githubusercontent.com/Dene33/notes-recognition/master/python-util-scripts/outRenamer.py">питоновский&nbsp;скрипт</a> в папку out и запускаем.</p>

<h3><strong>Быстрая установка и запуск на Линуксе</strong></h3>

<blockquote>
<p>sudo pip install aocr<br />
pip install tensorflow</p>

<p>git clone https://github.com/Dene33/notes-recognition<br />
cd notes-recognition<br />
unzip checkpoints.zip -d checkpoints</p>

<p>aocr test --visualize notesTest.tfrecords --max-width 1000 --max-height 61 --max-prediction 36 --full-ascii --model-dir ./checkpoints/checkpointsDL</p>
</blockquote>

<h3><strong>Тест на своём датасете</strong></h3>

<p>Чтобы протестировать на своих картинках, создаём папку с картинками. Максимальная высота картинок - 60, ширина - 1000. Создаём текстовый файл (например labels.txt)&nbsp;с лейблами такого формата:</p>

<blockquote>
<pre>
<code>./datasets/images/hello.jpg hello
./datasets/images/world.jpg world</code></pre>
</blockquote>

<p>где&nbsp;./datasets/images/hello.jpg - путь до картинки,&nbsp;hello - её лейбл. Какому символу какая нота соответствует&nbsp;<a href="https://github.com/Dene33/notes-recognition/blob/master/dictionary.txt">можно посмотреть тут</a>, где 1 столбец - лейблы, 2 - соответствующая нота или знак.</p>

<p>Затем,&nbsp;чтобы создать tfrecord из картинок выполняем:</p>

<blockquote>
<pre>
<code>aocr dataset ПУТЬ/К/labels.txt ПУТЬ/К/МОДЕЛИ/testing.tfrecords</code>
</pre>
</blockquote>

<p>Запускаем:&nbsp;</p>

<blockquote>
<p>aocr test --visualize ПУТЬ/К/testing.tfrecords --log-path ./log/log.log --max-width 1000 --max-height 61 --max-prediction 36 --full-ascii&nbsp;--model-dir ПУТЬ/К/checkpoints</p>
</blockquote>

<p>Примеры картинок из обучаемой выборки и соответствующих лейблов:</p>

<p><img alt="" src="https://i.imgur.com/Or25fJU.png" style="height:60px; width:242px" />&nbsp;MRRRROT:3+)R*</p>

<p><img alt="" src="https://i.imgur.com/wqkL3u8.png" style="height:60px; width:333px" />&nbsp;MRRN;RK+3R&quot;QR&lt;L+6</p>

<p><img alt="" src="https://i.imgur.com/bnBS1xb.png" style="height:60px; width:182px" />&nbsp;MSSO6S4&#39;</p>

<p>Ссылка на .tfrecord который использовался для обучения модели:&nbsp;<a href="https://drive.google.com/file/d/1wd716Lg6Uz5Vxr6x-vEeoLKMb09YapPL/view?usp=sharing">https://drive.google.com/file/d/1wd716Lg6Uz5Vxr6x-vEeoLKMb09YapPL/view?usp=sharing</a></p>

<h3><strong>TODO</strong></h3>

<p>1. Экспорт SaveModel для Tensorflow</p>

<p>2. Конвертация в MIDI</p>

<p>3. Сегментация листа на такты и обратная сборка всей структуры после прохода распознаванием по каждому сегменту</p>

<p>4. Поднять Tensorflow Serving</p>

<p>5. Разметка датасета под распознавание фотографий и более широкого спектра символов</p>

<p>&nbsp;</p>

<p>ETH-wallet:&nbsp;0x136f0a3d6f3Db9db3b742153a396B8b47721Bb24</p>
