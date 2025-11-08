import React from 'react'
import './ContactList.css'

const ContactList = ({ contacts, updateContact, updateCallback }) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            const response = await fetch(`http://127.0.0.1:5000/delete-contact/${id}`, options)
            if (response.status === 200) {
                updateCallback()
            } else {
                console.error('Failed to delete contact')
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div className="contact-list-container">
        <h2>Contacts</h2>
        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {contacts.map((contacts) => (
                    <tr key={contacts.id}>
                        <td>{contacts.firstName}</td>
                        <td>{contacts.lastName}</td>
                        <td>{contacts.email}</td>
                        <td>
                            <button onClick={() => updateContact(contacts)}>Update</button>
                            <button onClick={() => onDelete(contacts.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default ContactList