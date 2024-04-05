const addButton = document.getElementById('add');
const subButton = document.getElementById('sub');
const mulButton = document.getElementById('mul');
const Display = document.getElementById('display');
let x = 0;

addButton.addEventListener('click', () => {
  if(x<100){
    x++;
  }
  Display.textContent = x;
});

subButton.addEventListener('click', () => {
  if(x>0){
    x--;
  }
  Display.textContent = x;
});

mulButton.addEventListener('click', () => {
  
  if(x<51){
    x=x*2;
  }
  Display.textContent = x;
});