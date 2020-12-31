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


select * -- to find latest version of the article
from wiki_page
where article_id = 1
and is_main = TRUE
and version = (select max(version)
               from wiki_page
               where article_id = 1
               group by article_id);

update wiki_page -- to update is_main flag whenever new article is added
set is_main = 0
where article_id = 3
and version != (select max(version)
                from wiki_page
                where article_id = 3
                group by article_id);


delete from wiki_page; -- to truncate the table

drop table wiki_page; -- to drop the table
