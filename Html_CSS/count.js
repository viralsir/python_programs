  let count=0;
     function counter(){
       count++;
       if (count %10 ==0)
       {
            alert(`count reach to ${count}`);
       }
       document.querySelector("h1").innerHTML=count;

     }
     document.addEventListener('DOMContentLoaded',function(){
         document.querySelector("button").onclick=counter;
     })