def simple_generator():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# Simple Generator 
def count_up_to(n):
    count=1
    while count<=n:
        yield count
        count+=1
counter=count_up_to(5)
print(next(counter))
print(next(counter))
#square 
def square_numbers(n):
    for i in range(n):
        yield i*i
squares = square_numbers(5)
print(next(squares))
print(next(squares))
print(next(squares))
#streaming large data
def stream_vedio(chunks):
    for chunk in chunks:
        yield chunk
vedio_chunks=["chunk1","chunk2","chunk3"]
player=stream_vedio(vedio_chunks)
print(next(player))
#infinite news feed
def fetch_posts():
    post_id=1
    while True:
        yield f"Post {post_id}"
        post_id += 1    
post_generator = fetch_posts()
print(next(post_generator))
print(next(post_generator))

#log file processing


#music playlist
def music_playlist(songs):
    for song in songs:
        yield song
playlist=music_playlist(["Song1", "Song2", "Song3"])
print(next(playlist))
print(next(playlist))
print(next(playlist))