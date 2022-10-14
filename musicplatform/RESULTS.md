# Queries and results

#### Create some artists

```http
  Artist.objects.create(stage_name="Karem", social_link="https://codeforces.com/")
```

```http
  <Artist: Karem>
```

#### List down all artists

```http
  Artist.objects.all()
```

```http
  <QuerySet [<Artist: Ahmed>, <Artist: Amro>, <Artist: Karem>, <Artist: Sara>]>
```

#### List down all artists sorted by name

```http
  Artist.objects.all().order_by("-stage_name")
```

```http
  <QuerySet [<Artist: Sara>, <Artist: Karem>, <Artist: Amro>, <Artist: Ahmed>]>
```

#### List down all artists whose name starts with a

```http
  Artist.objects.filter(stage_name__startswith="a").values()
```

```http
  <QuerySet [{'id': 2, 'stage_name': 'Ahmed', 'social_link': 'https://codeforces.com/'}, {'id': 1, 'stage_name': 'Amro', 'social_link': 'https://codeforces.com/'}]>
```

#### In 2 different ways, create some albums and assign them to any artists

```http
  d = datetime.datetime(2023, 11, 11, 1, 2, 32, 5456)
  Album.objects.create(name="A2",release_datetime=d,cost=5837.42,artist=Artist.objects.get(pk=1))

  Album.objects.create(name="B1", release_datetime=d,cost=341.25)
  a = Album.objects.get(pk=3)
  a.artist = Artist.objects.get(pk=2)
  a.save()
```

```http
  <Album: A2>

  <Album: B1>
```

#### Get the latest released album

```http
  Album.objects.all().order_by("-release_datetime")[0]
```

```http
  <Album: B1>
```

#### Get all albums released before today

```http
  Album.objects.filter(release_datetime__lt=dd)
```

```http
  <QuerySet [<Album: C1>, <Album: C2>]>
```

#### Get all albums released today or before but not after today

```http
  Album.objects.filter(release_datetime__lte=dd)
```

```http
  <QuerySet [<Album: C1>, <Album: C2>, <Album: C3>]>
```

#### Count the total number of albums

```http
  Album.objects.all().count()
```

```http
  6
```

#### In 2 different ways, for each artist, list down all of his/her albums

```http
  for i in Artist.objects.all():
     print(i.stage_name)
     print(i.albums.all())

  for i in Artist.objects.all():
     print(i.stage_name)
     print(Album.objects.filter(artist=i))
```

```http
  Ahmed
  <QuerySet [<Album: B1>]>
  Amro
  <QuerySet [<Album: A1>, <Album: A2>]>
  Karem
  <QuerySet []>
  Sara
  <QuerySet []>
```

#### List down all albums ordered by cost then by name (cost has the higher priority)

```http
  Album.objects.all().order_by("cost","name")
```

```http
  <QuerySet [<Album: A1>, <Album: B1>, <Album: C1>, <Album: C2>, <Album: C3>, <Album: A2>]>
```
