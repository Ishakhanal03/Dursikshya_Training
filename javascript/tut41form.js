const displayMsg=(msg,id,colorname)=>{
    document.getElementById(id).innerHTML=msg
    document.getElementById(id).style.color=colorname



}

const fnameValidate=()=>{
    const first_name=document.getElementById('fname').value
    if(first_name==""){
        displayMsg("First Name is Mandatory","fnameMsg","red")
        return false
    }
    else if(!first_name.match(/^([a-zA-Z])+$/)){
        displayMsg("First Name contains alphabets only","fnameMsg","red")
        return false
    }

    else if(first_name.length<3){
        displayMsg("First Name be must be more than 2 characters","fnameMsg","red")
        return false
    }
    else{
        displayMsg("Valid First Name",'fnameMsg','green')
        return true
    }
}

const lnameValidate=()=>{
    const last_name=document.getElementById('lname').value
    if(last_name==""){
        displayMsg("Last Name is Mandatory","lnameMsg","red")
        return false
    }
    else if(!last_name.match(/^([a-zA-Z])+$/)){
        displayMsg("Last Name contains alphabets only","lnameMsg","red")
        return false
    }
     else if(last_name.length<3){
        displayMsg("Last Name be must be more than 2 characters","lnameMsg","red")
        return false
    }
    else{
        displayMsg("Valid last Name",'lnameMsg','green')
        return true
    }
}

const emailValidate=()=>{
    const email=document.getElementById('email').value
    if(email==""){
        displayMsg("Email is mandatory.","emailMsg","red")
        return false
    }

    else if(!email.match(/^([a-z0-9])[a-z0-9\#\-\.]+\@+([a-z])+\.+([a-z])+$/)){
        displayMsg("Invalid Email format","emailMsg","red")
        return false
    }

    else{
        displayMsg("Valid Email","emailMsg","green")
        return true
    }


}

const pwdValidate=()=>{
    const password=document.getElementById("pwd").value
    if(pwd==""){
        displayMsg("password is mandatory","pwdMsg","red")
        return false
    }

    else if(!password.match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\@\#\!\?]).{8,50}$/)){
        displayMsg(" Weak password,Password must contain Uppercase and Lowercase alphabets,special characters and numeric values.","pwdMsg","red")
        return false
     }

    else{
        displayMsg("Strong password","pwdMsg","green")
        return true

    }
}

const validform=()=>{
    if(fnameValidate()&&lnameValidate()&&emailValidate()&&pwdValidate()){
        return true
    }
    else{
        return false
    }
}