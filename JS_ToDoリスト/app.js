let command = prompt('コマンドを入力してください(new, list, delete, quit)');
const task=[];

while(command != "quit"){
    if(command === "new"){

        command = prompt('新しいタスクを入力してください');
        task.push(command);
        console.log(`「${command}」を追加しました`);

    }else if(command === "list"){

        console.log("***********");
        for(let i=0; i<task.length;i++){
            console.log(`${i}: ${task[i]}`);
        }
        console.log("***********");

    }else if(command === "delete"){

        command = parseInt(prompt('取り消しするインデックスを入力してください'));
        if(!Number.isNan(command)){
            console.log(`「${task[command]}」を取り消しました`);
            task.splice( command, 1 );
        }else{
            console.log("有効なインデックスを入力してください");
        }
        

    }
    command = prompt('コマンドを入力してください(new, list, delete, quit)');
}

console.log("アプリを終了します");