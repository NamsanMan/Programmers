from collections import deque

def conv(s):
    for a, b in (("C#","c"), ("D#","d"), ("E#","e"), ("F#","f"),
                 ("G#","g"), ("A#","a"), ("B#","b")):
        s = s.replace(a, b)
    return s

def solution(m, musicinfos):
    m = conv(m)
    music_list = []     # [["음악 full code 1", "제목 1"], ["음악 full code 2", "제목 2"], ...]
    for i in range(len(musicinfos)):
        row = musicinfos[i].split(",")
        row[3] = conv(row[3])
        duration = (int(row[1].split(":")[0]) * 60 + int(row[1].split(":")[1])) - (int(row[0].split(":")[0]) * 60 + int(row[0].split(":")[1]))
        code = ""
        while len(code) < duration:
            code += row[3][len(code) % len(row[3])]
        music_list_row = []
        music_list_row.append(code)
        music_list_row.append(row[2])
        music_list.append(music_list_row)
    
    candidates_list = []        # [[길이 1, "제목 1"], [길이 2, "제목 2"], ...]
    for i in range(len(music_list)):
        match = False
        time_len = len(music_list[i][0])
        queue = deque(music_list[i][0])
        while queue:
            if queue[0] == m[0]:
                if len(queue) >= len(m):
                    for j in range(len(m)):
                        if m[j] != queue[j]:
                            break
                    else:
                        match = True
            if match == True:
                candidates_list_row = []
                candidates_list_row.append(time_len)
                candidates_list_row.append(music_list[i][1])
                candidates_list.append(candidates_list_row)
                break
            else:
                queue.popleft()
    if not candidates_list:
        return "(None)"
    else:
        new = sorted(candidates_list, key=lambda x: -x[0])
        return new[0][1]