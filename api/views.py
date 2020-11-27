from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from api.models import Publication, Pop30, Poporder
from django.conf import settings
#
class Pop30Info():
    def get_html(self):
        pop = Pop30.objects.latest('created_at')
        pop30 = Poporder.objects.filter(pop30=pop.id).values('song__name', 'song__image')
        html = '<table>'

        for x in range(0, len(pop30), 2):
            if x == 0:
                html += '<tr>'
                html += '<td colspan="2" style="align:center"><img alt="" src="{}/{}" width="130" height="130"></td>'.format(
                    settings.MEDIA_URL,
                    pop30[x]['song__image'])
                html += '</tr>'
            else:
                html += '<tr>'
                html += '<td><img alt="" src="{}/{}" width="100" height="100"></td>'.format(settings.MEDIA_URL,
                                                                                            pop30[x]['song__image'])
                html += '<td><img alt="" src="{}/{}" width="100" height="100"></td>'.format(settings.MEDIA_URL,
                                                                                            pop30[x + 1]['song__image'])
                html += '</tr>'
        html += '</table>'

        return html

class HomeView(ListView, Pop30Info):
    def get(self, *args, **kwargs):
        p = Publication.objects.order_by('-created_at')
        lastvideo = Pop30.objects.order_by('-created_at').first()
        p3=Pop30Info()
        html = p3.get_html()

        context = {
            'object': p,
            'html': html,
            'lastvideo':lastvideo.youtube
        }

        return render(self.request, 'home.html', context)

# def albums(request):
#     return render(request, "albums.html")

# class AlbumesView(ListView):
#     model = Album
#     paginate_by = 10
#     template_name = "examples.html"


class AlbumsView(View, Pop30Info):
    def get(self, *args, **kwargs):
        p = Publication.objects.filter(category='album').all()
        pop = Pop30.objects.latest('created_at')
        p3 = Pop30Info()
        html = p3.get_html()


        lastvideo = Pop30.objects.order_by('-created_at').first()
        context = {
            'object': p,
            'html':html,
            'lastvideo':lastvideo.youtube
        }

        return render(self.request, 'albums.html', context)

class NewsView(View):
    def get(self, *args, **kwargs):
        p = Publication.objects.filter(category='news').all()
        pop = Pop30.objects.latest('created_at')
        p3 = Pop30Info()
        html = p3.get_html()
        lastvideo = Pop30.objects.order_by('-created_at').first()

        context = {
            'object': p,
            'html': html,
            'lastvideo':lastvideo.youtube
        }

        return render(self.request, 'news.html', context)

class ArticleView(View):
    def get(self, *args, **kwargs):
        p = Publication.objects.filter(category='opinion').all()
        pop = Pop30.objects.latest('created_at')
        p3 = Pop30Info()
        html = p3.get_html()
        lastvideo = Pop30.objects.order_by('-created_at').first()

        context = {
            'object': p,
            'html': html,
            'lastvideo':lastvideo.youtube
        }

        return render(self.request, 'news.html', context)

class  Pop30View(View):
    def get(self, *args, **kwargs):
        pop = Pop30.objects.latest('created_at')
        pop30 = Poporder.objects.filter(pop30=pop.id).values(
            'song__name',
            'song__image',
            'song__youtube','song__album__name'
        )
        p3 = Pop30Info()
        html = p3.get_html()
        lastvideo = Pop30.objects.order_by('-created_at').first()

        context = {
            'object': pop30,
            'html': html,
            'lastvideo': lastvideo.youtube
        }

        return render(self.request, 'pop30.html', context)