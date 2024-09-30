function op_skip(pos,video_len,op_start,op_end){
    if (pos > video_len) return video_len;
    else if (pos < 0) return 0;
    else if (op_start <= pos && pos <= op_end) return op_end;
    
    return pos;
}

function solution(video_len, pos, op_start, op_end, commands) {
    let answer = '';
    
    let split_pos = pos.split(":").map(x => parseInt(x));
    let split_op_start = op_start.split(":").map(x => parseInt(x));
    let split_op_end = op_end.split(":").map(x => parseInt(x));
    let split_video_len = video_len.split(":").map(x => parseInt(x));

    pos = split_pos[0] * 60 + split_pos[1];
    op_start = split_op_start[0] * 60 + split_op_start[1];
    op_end = split_op_end[0] * 60 + split_op_end[1];
    video_len = split_video_len[0] * 60 + split_video_len[1];

    for (let i = 0; i < commands.length; i++) {
      
        pos = op_skip(pos,video_len,op_start,op_end)
        
        if (commands[i] == "next") pos += 10;
        else pos -= 10;
        
        pos = op_skip(pos,video_len,op_start,op_end)
    }

    let hour = parseInt(pos / 60);
    let min = pos % 60;

    if (hour < 10) hour = `0${hour}`;
    if (min < 10) min = `0${min}`;
    answer = `${hour}:${min}`;
    
    return answer;
}