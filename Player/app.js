const container = document.querySelector('#container');

const baseurl = "https://www.buffaloes.co.jp/media/sites/6/images/team/player/2023/";



let i = 0;
const interval = setInterval(function() {

  const player = document.createElement('div');
    player.classList.add('player')
    const label = document.createElement('div');
    label.innerText = `#${i}`;
    const newImg = document.createElement('img');
    newImg.src = `${baseurl}${i}.jpg`;

    newImg.onload = function(){
        player.appendChild(newImg);
        player.appendChild(label);
        container.appendChild(player);
    }



  i++;
  if (i > 100) {
    clearInterval(interval); 
  }
}, 100); 
