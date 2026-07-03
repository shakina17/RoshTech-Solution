/* Smooth Scrolling */

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e){
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        target.scrollIntoView({
            behavior: "smooth"
        });
    });
});


/* Contact Form Validation */

const form = document.getElementById("contactForm");
const errorMsg = document.getElementById("errorMsg");

form.addEventListener("submit", function(e){
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const message = document.getElementById("message").value;

    if(name === "" || email === "" || phone === "" || message === ""){
        errorMsg.textContent = "Please fill all fields!";
    }
    else if(!email.includes("@")){
        errorMsg.textContent = "Enter valid email!";
    }
    else{
        errorMsg.textContent = "";
        alert("Message sent successfully 🚀");
        form.reset();
    }
});