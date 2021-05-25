 function hello(){
      let heading=document.querySelector("h1");
      if(heading.innerHTML == "hello")
      {
        heading.innerHTML="Good Bye";
      }
      else
      {
        heading.innerHTML="hello";
      }

    }
    document.addEventListener('DOMContentLoaded',function (){
      document.querySelector("button").onclick=hello;
    })
