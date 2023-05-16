---
title: Gossip, Advice, Jokes
layout: collection
body: Trees get lonely too, so we'll give him a little friend. Here's something that's fun. There is immense joy in just watching - watching all the little creatures in nature. The secret to doing anything is believing that you can do it. Anything that you believe you can do strong enough, you can do. Anything. As long as you believe. God gave you this gift of imagination. Use it. Isn't that fantastic that you can create an almighty tree that fast? With something so strong, a little bit can go a long way. A thin paint will stick to a thick paint. If you don't like it - change it. It's your world. Fluff that up.
---

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
	{%- for post in collections.gossipAdviceJokes -%}
		<tr>
			<td class="table-title">
				  <a href="{{ post.url | url }}">
				  "{{ post.data.title }}"
					</a>
			</td>
		  <td class="table-author">
			 {%- for author in post.data.author -%}
			  	{{ post.data.author }}, 
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


