from django.shortcuts import render,redirect,get_object_or_404
from core.models import Movie,Video,Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def MovieList(request):
    query = request.GET.get("query","")
    movies = Movie.objects.all()
    movie_id = request.GET.get("movie",0)

    if query:
        movies = movies.filter(name__icontains=query)
    if movie_id:
        movies = movies.filter(movie_id=movie_id)
    context = {
    'movies':movies,
    "query":query,
    "movie_id":movie_id,
    }


    return render(request, 'movielist.html', context)

@login_required
def detail(request,pk):
    
    related_movies = Movie.objects.all().exclude(pk=pk)[0:4]
    movie = get_object_or_404(Movie,pk=pk)

   
    return render(request,"detail.html",{
        "movie":movie,
        "related_movies":related_movies,
        
    })

@login_required
def Playmovie(request,movie_id):
    # Lấy đối tượng Movie có tên là "The Matrix"
    movie = Movie.objects.get(uuid=movie_id)
    movie = Movie.objects.get(name=movie.name)

# Lấy ra queryset chứa tất cả các video liên kết với đối tượng Movie này
    videos = movie.video.all()

# Lấy ra địa chỉ của video đầu tiên trong queryset
    video_url = videos[0].file.url
    context = {
        "video_url":video_url,
    }
    try :
        return render(request, 'playmovie.html', context)
    except :
        return redirect("movie:movielist")
    

@login_required
def Tvshow(request):
    tv_shows_movies = Movie.objects.filter(kind__contains='TV Shows')
    return render(request,"movielist.html",{
        "movies":tv_shows_movies
    })

@login_required
def LatestMovie(request):
    movies = Movie.objects.filter(when__gte=2022)
    return render(request,"movielist.html",{
        "movies":movies,
    })

@login_required
def Mylist(request):
    related_movies = Movie.objects.all()[0:4]
    return render(request,"movielist.html",{
        "movies":related_movies,
    })
    