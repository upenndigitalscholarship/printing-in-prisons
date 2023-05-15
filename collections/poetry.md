---
title: Poetry
layout: collection
---
<div class="element-centered widest">
	<p><i>
		Curated by Whitney Trettien, originally posted June 1, 2023 and last edited June 1, 2023
	</i></p>
	<p>
		Nearly every newsletter or magazine issued from the press room at Eastern State contained poetry. There is poetry about the weather and baseball; on aging and advice; on patriotism and war. There are jokes about other incarcerated men. And there is minstrelsy and racism. Some of the verse is copied from other sources, often newspapers or books in the prison’s library. For instance, William Wordsworth makes an appearance in an issue of The Umpire, extolling the rise of the morning sun. So does children’s author Susan Chauncey Woolsey (pen name Susan Coolidge), on the powers of beginning again. But by far the most engaging verse is always written by those incarcerated at Eastern State. Unfortunately, we do not know many of their real names; prison rules dictated that incarcerated authors must published under their inmate number or a nickname. But by tracking these pseudonyms across the printed corpus, we can gain a fuller glimpse of their interests and oeuvre.
	</p>
	<p> 
		Below, learn more about some of the prison’s most prolific twentieth-century poets, or dig into the data yourself using the index of verse at the bottom of this page.
	</p>
	<h3>“Spider”</h3>
	<p>
		From 1913 on, the man nicknamed “Spider” was one of The Umpire’s most prolific writers of verse. He was also one of the funniest and most real, penning weekly verse that spoke directly to his incarcerated friends, their foibles, and local happenings in and around Eastern State. Sometimes his advice is touching. In “Kindness in Our Hidden City,” he encourages others who find themselves locked within the Eastern State’s “Gray Stone Walls” to offer “a nice kind word to a pal that’s blue / How it shortens the day and helps him thro’. / And don’t forget the lifetime men / Show them a kindness whene’er you can.” But he is not afraid to razz his colleagues, either. Throughout the baseball season, Spider can be found ragging on umpires and mocking the inflated bluster of the players. “A gang of has beens,” he writes in the June 25, 1913 issue, “you struck a snag / From this time on, you better play tag.”
	</p>
	<p>Read Spider’s poetry here .</p>
	<h3>“J.P.C”</h3>
	<p>
		J.P.C. must have been involved in editing The Umpire and operating the printing press at Eastern State, since many of his poems offer insight into these processes. A humorous reflection published in the May 14, 1913 issue, titled “The Editor’s Nightmare,” is especially apt. In it, he imagines a “Timmie” falling asleep “on the Press room floor / Having written sos much he could write no more.” Timmie dreams he is riding “the ‘Umpire’s’ train”: a nightmarishly inky engine full of rude editors and botched engravings, each line an in-joke about the newspaper’s editorial team. He wakes up, “his clothes soaked and his hair standing high,” begging to never have to write for The Umpire again.
	</p>
	<p>Read J. P. C.’s poetry here.</p>

</div>

<div id="articles" class="widest">
	<table class="list">
	<tr>
	  <td><b>title</b></td>
		<td><b>author </b></td>
		<td><b>year</b></td>
		<td><b>newspaper</b></td>
		<td><b>month</b></td>
		<td><b>day</b></td>
		<td><b>tags</b></td>
	</tr>
	{%- for post in collections.baseball -%}
	<tr>
	  <td class="table-title">
	  <a href="{{ post.url | url }}">
	  {{ post.data.title }}
		</a>
		</td>
	  <td class="table-author">
		 {%- for author in post.data.author -%}
		  	{{ author }}, 
		  {%- endfor -%}
	   </td>
	<td class="table-year">{{ post.data.year }}</td>
		<td class="table-newspaper">{{ post.data.newspaper }}</td>
		<td class="table-month">{{ post.data.month }}</td>
		<td class="table-day">{{ post.data.day }}</td>
		<td class="table-tag">{%- for tag in post.data.tags -%}
		  	{{ tag }}, 
		  {%- endfor -%}</td>
	</tr>
	{%- endfor -%}
	</table>
</div>


