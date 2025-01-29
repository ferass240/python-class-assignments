
    function addtask(){
        var task = document.getElementById("task").value;
        if (task !==""){
            var newTask = document.createElement("div");
            newTask.classList.add("task");
            newTask.innerHTML = task;

            var deleteButton = document.createElement("button");
            deleteButton.classList.add("delete-btn");
            deleteButton.innerHTML = "Delete";
            newTask.appendChild(deleteButton);
            // Attach an event listener to the delete button
            deleteButton.addEventListener("click", function() {
            newTask.remove(); // Remove the task when the delete button is clicked
            });
            document.getElementById("taskList").appendChild(newTask);
            document.getElementById("task").value = "";

        } else {
            alert("Please enter a task.");
        }
       

   }    
