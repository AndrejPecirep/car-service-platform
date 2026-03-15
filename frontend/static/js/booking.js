document
.getElementById("bookingForm")
.addEventListener("submit", async (e)=>{

e.preventDefault()

const data={
vehicle_id:document.getElementById("vehicle").value,
service_id:document.getElementById("service").value,
staff_id:document.getElementById("staff").value,
start_time:document.getElementById("start").value,
end_time:document.getElementById("end").value
}

try{

await apiRequest("/booking","POST",data)

alert("Appointment created")

}catch(err){

alert("Error creating booking")

}

})