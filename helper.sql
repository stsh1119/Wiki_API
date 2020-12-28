create table wiki_page( article_id integer,
                        title text not null,
                        text text,
                        version integer,
                        is_main integer,
                        primary key (article_id, version)
                       );


select *  -- to find all articles
from wiki_page;

select * -- to find all versions for a specific article
from wiki_page
where article_id = 1;

insert into wiki_page(article_id, title, text, version, is_main)
values(1,'Blah blah', 'Body of this article', 2, TRUE);

update wiki_page
set is_main = FALSE
where is_main = 1 and  version != 2;

drop table wiki_page;

select * -- to find latest version of the article
from wiki_page
where article_id = 1
and is_main = TRUE
and version = (select max(version)
               from wiki_page
               where article_id = 1
               group by article_id);