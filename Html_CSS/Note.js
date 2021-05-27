function multiplyBy()
{
        num1 = document.getElementById("firstNumber").value;
        num2 = document.getElementById("secondNumber").value;
        num3 = document.getElementById("ThirdNumber").value;
        num4 = document.getElementById("FourNumber").value;
        num5 = document.getElementById("FiveNumber").value;
        num6 = document.getElementById("SixNumber").value;
        num7 = document.getElementById("SevenNumber").value;
        document.getElementById("result").innerHTML = (10 * num1)+ (20*num2) + (50*num3) +(100*num4)+(200*num5)+(500*num6)+(2000*num7);
        if(num6!='')
        {
                display_notes(num6,"500");
        }
        if(num7 != '')
        {
                display_notes(num7,"2000");
        }
        if(num4 != '')
        {
                display_notes(num4,"100");
        }
        console.log(num7);
}
function display_notes(num6,notes)
{
         let no_notes=document.querySelector("#no_notes")

         for (let i = 0; i < num6; i++)
                {
                    let td1=document.createElement("td")
                    td1.innerHTML=notes;
                    let td2=document.createElement("td");
                    td2.innerHTML="<input type=text size=20>";
                    let tr=document.createElement("tr");
                    tr.append(td1);
                    tr.append(td2);
                    no_notes.append(tr);
                }
}
