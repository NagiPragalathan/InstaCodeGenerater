Title=""
VidTitle=""
Video_Title=""
iframe=""
def assgin(title,video_Title,Iframe):
    global Title,Video_Title,VidTitle,iframe
    Title=title
    VidTitle=Title
    Video_Title = video_Title
    iframe = Iframe

    index1=f"""<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../CSS/index.css">
        <title>{Title}</title>
    </head>
    <body>
        <nav class = "nav" id="nav">
                <div class="img" onclick="redirect(1)"></div>

            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="https://m.youtube.com/channel/UCwqqgoHCYOo2n9bERHQMK7A">YouTube</a></li>
                <li><a href="https://nagipragalathan.github.io/Personal_website/social.html">Contact</a></li>
                <li><a href="https://nagipragalathan.github.io/Personal_website/about.html">About</a></li>
                <div class="none">

                </div>
            </ul>
            <button class="btn" id="btn" onclick="btn(1)">Btn</button>
        </nav>
        <button class="btn2" id="btn2" onclick="btn(2)"></button>

        <div class="sidenav" id="sidenav">
            <div class="btns" id="btns">

            </div>
        </div>
        <button class="sbtn" id="sbtn" onclick="ctrl()"></button>

        <div class="total">
            <div class="phodo">
                
            </div>
            <div class="alain">
                <div class = "phodo1"></div>
                <div class="contant">
                    <h1 class="title">{VidTitle}</h1>
                    <div class="cbtn">
                        <button class="pre" onclick="LRbtn('{Title}',1)"></button>
                        <button class="next" onclick="LRbtn('{Title}',2)"></button>
                    </div>
                    <div class="video">
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                        <h2 style="color: #9d9aa3;margin-bottom: 10px;">{Video_Title}</h2>
                        { iframe }
                        <span></span>

                                            <!-- Output -->
                    </div>
                    <hr>
                    <h1 style = "margin-top: 28px;color: #ff4235;">Output</h1>
                    <div class="output">
                        <h1>The final output is : </h1>
                        <span class="span1"></span>
                        <p class="text1">"""

                                # {Output}
                            
                        
    index2 = """                    </p>
                    </div>



                    <hr>
                    <h1 style="color: #ff4235;">code</h1>
                    <div class="output">
                        <h1>Magic Code :</h1>
                        <span class="span1"></span>
                        <div class="text1">


    """

                                    # {Fullcode}

    index3 = """ </div>
                        <button class="code" onclick="newc()">Try It The magic...</button>
                    </div>

                    <hr>
                    <div class="step">
                        <h1 style="color: #a59392;margin-left: 17px;">Steps Of The code</h1>
                        <div class="steps">
                        <span class="span2"></span>
    """
                                    
                                    
                                        # {Steps}
    index4 = """</div>
                    </div>
                    <hr>
                    <div class="output">
                        <h1>Edit and Try Your self :)</h1>
                        <span class="span1"></span>
                        <textarea class="textforcode" id="textforcode" cols="30" rows="10">"""
                        
                        
                                        # {RuningCode}
                                        
    index5 = """ </textarea>
                        <button class="code" onclick="redirect(3)">Try Yourself >></button>
                    </div>
                    <hr>
                    <h1 style="margin-top: 26px;margin-bottom: 36px;font-family: cursive;color: yellowgreen;text-shadow: 9px 5px 5px black;">Thank You For visiting</h1>
                    <div class="per">
                        <span></span>
                        <div class="insta" >
                            <div class="imag">
        
                            </div>
                            <h1>Bug Breaker</h1>
                            <div class="detial">
                            
                                    <h2>Account Maintainer :</h2>
                                    <h3> Nagi Pragalathan.N</h3>
                                    About :<a href="">https://nagipragalathan/about</a>
                                    contact Me :<a href="https://nagipragalathan.github.io/Personal_website/social.html">https://nagipragalathan/contact</a>
                                
                            </div>
                            <div class="qr">

                            </div>
                        </div>
                        <div class="About">
                            <h1>About</h1>
                            <div class="p">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo recusandae saepe, accusantium ad nulla vero. Atque, sed. Aperiam odio voluptatibus sapiente eveniet saepe reiciendis ad minima? Ut totam numquam doloremque?</p>
                            </div>
                            <button class="Follow" onclick="redirect(1)"></button>
                        </div>
                    </div>
                    <div class="last">
                        <h1 style="font-family: cursive;font-size: 24px;color: antiquewhite;">Visite our Other Projects</h1>
                        <button class="git" onclick="redirect(2)" >Git Link</button>
                    </div>
                </div>
            </div>
        </div>

    <script src="../JS/Values.js"></script>

    <script>
        
        var count=0;
        var indect1 = document.getElementById("btn2");
        var btnn = document.getElementById("sbtn");


        function ctrl(){
            var snav = document.getElementById("sidenav");
            count++;
            if(count%2 == 1){
                btnn.style.left="259px";
                snav.style.width="243px";
                btnn.style.left="259px";
                indect1.style.visibility="hidden";

            }
            else{
                indect1.style.visibility="visible";
                snav.style.width="0px";
                btnn.style.left="18px";

            }
        }
        
        function btn(a){
            var indect = document.getElementById("btn");
            var nav = document.getElementById("nav");
            if(a==1){
                indect.style.transform="inherit";
                nav.style.transform="translateY(-276px)";
                nav.style.visibility="hidden";
                btnn.style.transition="1s";
                btnn.style.visibility="visible";
                indect1.style.visibility="visible";
                nav.style.transition="1s";
            }
            else{
                nav.style.visibility="visible";
                indect1.style.visibility="hidden";
                btnn.style.visibility="hidden";
                btnn.style.transition="0s";
                indect.style.visibility="visible";
                nav.style.transform="rotate3d(1, 1, 1, 119deg)";
                nav.style.transform="rotate3d(1, 1, 1, 360deg)";
                indect.style.transform="none";

            }

        }
        function redirect(a){
            if(a==1){
                window.location.href = "https://wwww.instagram.com/bug_breaker/"
            }
            if(a==2){
                window.location.href = "https://github.com/NagiPragalathan/"
            }
            if(a==3){
                window.location.href = "../HTML/w3school.html"
            }
        }
        var textarea = document.getElementById("textforcode");
        var code = textarea.textContent; 
        localStorage.setItem("pycode",code);
        function newc(){
            var code = textarea.textContent; 
            localStorage.setItem("pycode",code);
            window.location.href = "../HTML/codeViewr.html"
        }
    </script>
    </body>
    </html>



    """
    return [index1,index2,index3,index4,index5]