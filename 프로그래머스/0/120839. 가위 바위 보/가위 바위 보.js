function solution(rsp) {
    const winObj = {
        2:'0',
        0:'5',
        5:'2',
    }
    
    return rsp.split('').reduce((acc,cur) => {
        return acc += winObj[cur];
    },'');;
}