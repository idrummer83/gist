# gist

Разработать веб приложение для работы со сниппетами (фрагментами) кода, аналогичное https://gist.github.com/. 
Пользоваться сервисом можно только анонимно без заведения учетных записей.
Сниппеты могут быть публичными, которые видны всем пользователям и скрытыми, которые доступны только по секретной 
ссылке и в списке сниппетов отсутствуют.

1 сниппет может состоять из нескольких фрагментов кода. Форма отправки сниппетов должна позволять добавлять код 3 способами: 

вставкой кода в textarea, загрузкой файла и через указание http ссылки на файл, переход по которой должен сделать 
backend при обработке формы. 
Форма должна быть динамической, то есть можно создать 1 сниппет, где, например, 2 фрагмента будут добавлены через 
вставку кода, 4 через загрузку файла и еще 5 через внешние ссылки. После создания сниппета пользователя нужно 
перенаправить на страницу с этим сниппетом. Редактировать и удалять сниппеты нельзя. У каждого сниппета можно 
указать язык программирования, если он не указан, то сервис должен попытаться определить его самостоятельно 
по расширению файла или через shebang. Список поддерживаемых языков можно ограничить, например, 5 популярными языками.

На главной странице сервиса должен отображаться список сниппетов, отсортированных по времени добавления с постраничным выводом.
По каждому сниппету видно только время его добавления, сколько в нем файлов и первые 10 строк из первого файла. 
При переходе на страницу со сниппетом видны уже все полные файлы с подсветкой синтаксиса (для этого нужно использовать 
готовую библиотеку, например https://highlightjs.org/) Также на главной странице должна отображаться статистика по 
используемым языкам в сниппетах.
