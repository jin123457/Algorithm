function solution(my_string) {
    const consonant = ['a', 'e', 'i', 'o', 'u'];
    
    for(const word of consonant) {
        my_string = my_string.replaceAll(word,'');
    }
    
    return my_string;
}