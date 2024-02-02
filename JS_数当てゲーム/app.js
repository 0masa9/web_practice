let maximum = parseInt(prompt('数字を入力してください'));

while(!maximum){
    maximum=parseInt(prompt('エラーが起きました。有効な数字を入力してください'))
}

const targetNum = Math.floor(Math.random()*maximum)+1;
console.log(targetNum);
let guess = parseInt(prompt('1つに数字を決めました。数字を当ててみてください'));

while(guess != targetNum){
    if (guess > targetNum){
        guess = parseInt(prompt('その数字より小さいです！もう一度当ててみてください：'));
    }else{
        guess = parseInt(prompt('その数字より大きいです！もう一度当ててみてください：'));
    }
}

console.log("正解！");