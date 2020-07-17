SELECT id
FROM public.courses
WHERE uni_id = 1 and course_code = 'COMP1202';

SELECT AVG(average_num) as average_for_all_mark_data
FROM public.marks
WHERE course_id = 1
GROUP BY course_id;