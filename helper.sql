create table wiki_page(title text not null,
                       text text,
                       created_when text not null,
                       is_main integer,
                       primary key (title, created_when));

select *
from wiki_page;

insert into wiki_page(title, text, created_when, is_main)
values('First article', 'Body of this article', '12-28-2020', TRUE);

update wiki_page
set is_main = FALSE
where title = 'First article'
and created_when = '12-27-2020';

drop table wiki_page;