{% extends "%blog_post_base.html" %}
{% block title %}Totally free website hosting with GitHub Pages + script magic{% endblock %}
{% block title_img %}freemoney_header.jpg{% endblock %}
{% block page_url %}free_page_hosting.html{% endblock %}
{% block publish_date %}2022-11-04{% endblock %}
{% block page_description %}f you are younger than me, the word “Geocities” might mean nothing. It’s 2022: surely there is still some corner of the internet to put up a modest static webpage for free?{% endblock %}
{% block metatags %}github pages,static hosting,hosting,webpage,python,CMS,jekyll,template,jinja{% endblock %}

{% block content %}


Long, long ago, having a personal website was the norm. If you are younger than me, the word “Geocities” might mean nothing. It’s 2022: surely there is still some corner of the internet to put up a modest static webpage for free?

We have also learned a lot as developers in the intervening years. Can we add some modern conveniences to make our static website work smoother?

This blog post itself serves as an example of how to combine the content generation power of a backend, with the benefits of static hosting.


##Who is this for?

You are a frontend web developer or designer who wants a free website, and is fine with tweaking some scripts and HTML.

Or if you are a layperson who just really, really wants a free website, you could also follow along, and maybe learn a bit about web templates and scripting.

This blog post is dedicated to those who love Python. If you don't know the language and libraries, then I'd recommend using a different toolkit mentioned below. I have used Python for this site and all my examples, but the same concepts should hold for your language of choice if you want to build something similar.

You might already have a static website, or a full CMS with a bunch of templates which you want to easily migrate to a cheaper server.


##Why have a static website?

For many websites, there is no need to change the content very often. A Content Management System (CMS) such as Wordpress or Django is overkill. All you need to do is send some HTML to the user.

One huge plus for static websites is security: my static site has stood strong for decades with zero maintenance, without needing libraries to be updated. Whilst a billion Wordpress sites have inevitably fallen to hackers, like wheat at harvest time.

My personal website has been useful for finding work over the years. There is nothing like having your own permanent home on the internet, which you can print on a business card, or send people a link to.

It’s also useful to be able to easily host your own files online: as test data for some project you are developing; or for providing downloadable content, such as Terms and Conditions or file packs for apps you are building.


##Moving beyond the pain of raw HTML

I have been hand-writing all the HTML on this blog for about a decade, since I saw no need to set up a CMS service, and I didn’t want to pay for hosting, or for my page to be covered in ads.

But as the amount of my content has grown, it has become a significant task to maintain. For example, the “share” widgets need to be updated when their APIs change. I created a lot of bugs and broken links from copy/pasting from old articles.


## Thank you GitHub Pages: free page hosting!

A friend was hosting my page, but a couple of years ago I decided to move my webpage to GitHub Pages, which is a totally free hosting service.

I am very happy with GitHub Pages, and it’s very easy to setup. You can setup your page right now:

[https://pages.github.com](https://pages.github.com)

However, I missed the features of a CMS, such as being able to use templates. It felt wrong to be constantly copy/pasting the same HTML around. Surely there must be a way to add some server-side processing?

Nope. It’s static pages only. I thought about running client-side Javascript to generate the page dynamically in the browser. But I didn't want to completely destroy my page's ability to be indexed by search engines - customers have found me via Google in the past.

Then I had the bright idea of using a script to generate raw HTML from some offline templates, and uploading the raw HTML generated files to GitHub Pages. It turns out someone has already done that much better than I ever would have. It’s a toolkit called Jekyll.


##Using Jekyll. Or not.

[https://jekyllrb.com](https://jekyllrb.com)

Jekyll is officially supported by GitHub as a plugin. It compiles down your website source files into a polished static website, ready to be pushed to GitHub.

It already does all that I need, plus much more: it comes with themes, navigation logic, and conversion of markdown notation to HTML.


###So why not use this?

Because I don’t want to learn some new languages and tools just to maintain my website.

And I also like “rolling my own”, and reinventing the wheel - it’s fun. 

Jekyll uses a stack of Ruby and YAML, and custom markup. I have never needed to learn these things. I would ideally be able to use Python and Jinja templates, just like I do on my beloved Django/Flask + Python stack of choice.


##What have I done here?

I have written a simple script to make a static website "feel" like a dynamic website, with many of the conveniences and powerful tempalting features of a CMS. I can use templates, Python, and any other processing and compiling I want to do. All those source files will be compiled down to a completely static website.


##How it works

You can follow along with the source for this site here: [https://github.com/jhud/jhud.github.io](https://github.com/jhud/jhud.github.io). All the templates and logic live in the github.io repository, along with the main website that you are reading now. No promises that my approach will be particularly portable or adaptable to general cases.

jhud.github.io is a synonym for my custom domain [www.disconnectionist.com](https://www.disconnectionist.com). So my entire website, plus the means to generate it, are all stored in the one git repository.


The folder structure looks like this:

```
jhud.github.io
  <all my website files, images etc.>
  index.html
  src
     <any HTML templates for the website>
  scripts
    build_static_site.py
```

That ```build_static_site.py``` script is the key to everything: it is a Python script which runs the Jinja2 templating library over everything in the src folder. This is the templating system I use for Flask or Django websites, to avoid needing to commit heinous DRY sins such as copy/pasting the same header and footer into every web page.

Whenever I update my templates, I run the ```build_static_site.py``` script, and it searches the ```src``` folder for HTML files. It applies Jinja templating to all the HTML files that it finds.

Then I do a git commit + push to github.

The nice part about Jinja is that if you have no template tags in your HTML (i.e. it is just plain HTML), then Jinja will just output the original file. So you can drag your existing static HTML website to the "src" folder, and replace pieces of boilerplate header and footer with Jinja templates at your leisure.

There is one extra trick here. We don't want to generate website HTML from our base Jinja template HTML files; they are purely for generating other pages, and so should never appear on the main page. So the base template files get the special prefix %, which tells the script not to copy them across to the final webpage folder.

When we run the script, all the final HTML files generated from the templates are copied down to the root of the jhud.github.io folder, ready to be viewed on the actual webpage. The files replace whatever was there before, leaving images and other files in the bsae folder intact.

Git commit + push to GitHub takes care of the versioning for us, so that only the files actually changed by the script will be uploaded to GitHub to be served.

It usually only takes about 20 seconds after a git push for the new content to go live.


## Your domain name: the not-free part

You will get a free website at <yourname>.github.io. Github is far from an embarrassing domain for a developer to have, but you might want your own custome domain name, like www.disconnectionist.com
	
You will need to buy this from one of the usual providers, and then you can link it to GitHub. [Instructions here](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)


## Future expansion

I slightly prefer using Markdown to HTML, so it's an obvious choice to add a Markdown-to-HTML conversion step in my script. This post was written in Markdown, but I did the conversion in a manual step this time.

It would also be nice to automatically create an RSS feed and "other stories" from the directory listing of my blog, and also to generate HTML lists from json on the main page, for things like "news".

As I add even more content to my site and start finding the process of maintaining it painful, I'll keep adding extra functionality to this script.

This system isn't limited to GitHub Pages: it can be transferred to any place where static files can be hosted.


## In summary

This little project puts a warm glow in my heart: not only have I got something for free, but I have also automated some tedious tasks out of my life for good.

Hopefully it can help you to setup your own static website a bit more conveniently.

{% endblock %}