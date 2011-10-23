\echo insert into django_content_type
insert into djangobot_task(
            "name", script, interval_days, interval_hours, interval_minutes, 
            next_execution, last_execution, status, last_result, enabled)
values            
  ('1. haal artikelen op'       ,'aggregator.aggregate.main()'               ,0,0,1, now(), to_date('01 Jan 2001', 'DD Mon YYYY'),'ready','not yet run',False)
 ,('2. generatewordindex'       ,'aggregator.generatewordindex.main()'       ,0,0,1, now(), to_date('01 Jan 2001', 'DD Mon YYYY'),'ready','not yet run',False)
 ,('3. generatekrantweight'     ,'aggregator.generatekrantweight.main()'     ,0,0,1, now(), to_date('01 Jan 2001', 'DD Mon YYYY'),'ready','not yet run',False)
 ,('4. generatecalculatedweight','aggregator.generatecalculatedweight.main()',0,0,1, now(), to_date('01 Jan 2001', 'DD Mon YYYY'),'ready','not yet run',False)
 ,('5. generatecloudweight'     ,'aggregator.generatecloudweight.main()'     ,0,0,1, now(), to_date('01 Jan 2001', 'DD Mon YYYY'),'ready','not yet run',False)
 ,('6. generateranking'         ,'aggregator.generateranking.main()'         ,0,0,1, now(), to_date('01 Jan 2001', 'DD Mon YYYY'),'ready','not yet run',False)
;
       