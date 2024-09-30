function solution(video_len, pos, op_start, op_end, commands) {
    let answer = '';
    
    let split_pos = pos.split(":");
    let split_op_start = op_start.split(":");
    let split_op_end = op_end.split(":");
    let split_video_len = video_len.split(":");

    if (parseInt(split_pos[0]) > 0)
      pos = parseInt(split_pos[0]) * 60 + parseInt(split_pos[1]);
    else pos = parseInt(split_pos[1]);

    if (parseInt(split_op_start[0]) > 0)
      op_start = parseInt(split_op_start[0]) * 60 + parseInt(split_op_start[1]);
    else op_start = parseInt(split_op_start[1]);

    if (parseInt(split_op_end[0]) > 0)
      op_end = parseInt(split_op_end[0]) * 60 + parseInt(split_op_end[1]);
    else op_end = parseInt(split_op_end[1]);

    if (parseInt(split_video_len[0]) > 0)
      video_len = parseInt(split_video_len[0]) * 60 + parseInt(split_video_len[1]);
    else video_len = parseInt(split_video_len[1]);

    for (let i = 0; i < commands.length; i++) {
      if (pos > video_len) pos = video_len;
      else if (pos < 0) pos = 0;
      else if (op_start <= pos && pos <= op_end) pos = op_end;

      if (commands[i] == "next") pos += 10;
      else pos -= 10;

      if (pos > video_len) pos = video_len;
      else if (pos < 0) pos = 0;
      else if (op_start <= pos && pos <= op_end) pos = op_end;
    }

    let hour = parseInt(pos / 60);
    let min = pos % 60;

    if (hour < 10) hour = `0${hour}`;
    if (min < 10) min = `0${min}`;
    answer = `${hour}:${min}`;
    
    return answer;
}