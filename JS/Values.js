let Pages = [ 
                "Day1", "Day2",
                "Day3", "Day4",
                "Day5"
            ]

var str = "";
for(i=0;i<Pages.length;i++){
    str=str+"<button class = 'butn' onclick=sidebutton('"+Pages[i]+"')>"+Pages[i]+"</button>";
}
document.getElementById("btns").innerHTML=str;

function sidebutton(str){
    window.location.href = str + ".html"
}

function LRbtn(pos,num){
    let index = Pages.indexOf(pos);
    if( num == 1 ){
        window.location.href = Pages[index-1]+".html"
    }else{
        window.location.href = Pages[index+1]+".html"
    }
}