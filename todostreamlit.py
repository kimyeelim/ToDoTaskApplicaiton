# Import necessary libraries
import streamlit as st

# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    ## The task to be added to the linked list
    def add_task(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_task(self, task):
        current = self.head
        previous = None

        while current is not None:
            if current.data == task:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                return  # Added return statement to exit the method after removing the task
            previous = current
            current = current.next

    def display_tasks(self):
        tasks = []
        current = self.head

        while current is not None:
            tasks.append(current.data)
            current = current.next

        return tasks
    
    # Create a Streamlit app
def main():
    st.title("To-Do List App with Linked List")

    # Retrieve or create a linked list object
    tasks_list = get_linked_list()

    # Sidebar for adding tasks
    task_input = st.sidebar.text_input("Add Task:")
    if st.sidebar.button("Add"):
        if task_input:
            tasks_list.add_task(task_input)
            # Display updated tasks
            st.write("## Your To-Do List:")
            tasks = tasks_list.display_tasks()
            if not tasks:
                st.write("No tasks yet. Add some tasks using the sidebar!")
            else:
                for i, task in enumerate(tasks, start=1):
                    st.write(f"{i}. {task}")

    # Sidebar for removing tasks
    task_to_remove = st.sidebar.text_input("Remove Task:")
    if st.sidebar.button("Remove"):
        if task_to_remove:
            tasks_list.remove_task(task_to_remove)
            # Display updated tasks
            st.write("## Your To-Do List:")
            tasks = tasks_list.display_tasks()
            if not tasks:
                st.write("No tasks yet. Add some tasks using the sidebar!")
            else:
                for i, task in enumerate(tasks, start=1):
                    st.write(f"{i}. {task}")

# Function to retrieve or create linked list object
def get_linked_list():
    session_state = st.session_state
    if 'tasks_list' not in session_state:
        session_state.tasks_list = LinkedList()
    return session_state.tasks_list

if __name__ == "__main__":
    main()
