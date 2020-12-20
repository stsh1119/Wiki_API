create table wiki_page(article_id integer primary key autoincrement, title text, text text, is_main integer);

select *
from wiki_page;

insert into wiki_page(title, text, is_main)
values('First article', 'Body of this article', 1);

update wiki_page
set is_main = 0
where article_id = 1;
