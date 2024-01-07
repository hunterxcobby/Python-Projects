### 1. **Persistency in Web Applications:**
   - **Definition:** Persistency refers to the ability of a web application to retain data between different executions. In other words, when the program is run again, it starts with all the objects that were created in a previous execution.
   - **Importance:** It ensures that the work done in a previous session is saved, allowing for continuity and retrieval of information.

### 2. **Types of Storage: File and Database:**
   - **File Storage:**
     - **Purpose:** Initial focus in this project is on file storage.
     - **Modularity:** Separating storage management from the model makes models modular and independent. This design allows for easier replacement of the storage system without having to recode the entire application.

### 3. **Use of Class Attributes:**
   - **Class vs. Instance Attributes:**
     - **Class Attributes:** Used for any object, providing a shared attribute among all instances of a class.
     - **Instance Attributes:** Not used in this context for three reasons:
       1. **Easy Class Description:** Class attributes make it easy to understand what a model should contain, enhancing readability.
       2. **Default Values:** Class attributes can provide default values for attributes, ensuring consistency.
       3. **Consistent Model Behavior:** Using class attributes facilitates maintaining consistent behavior for both file and database storage in the future.

### 4. **Benefits of Separation:**
   - **Modularity:** Separating storage management from the model enhances modularity, allowing for easier maintenance and changes.
   - **Flexibility:** This architecture enables the replacement of storage systems without extensive code modifications, providing flexibility for future upgrades or changes in technology.

In summary, persistency ensures data continuity across executions. File storage is initially focused on for modularity. Class attributes are preferred for easy description, default values, and consistent behavior across different storage systems.

Feel free to ask if you have specific questions or if you'd like further clarification on any of these points.