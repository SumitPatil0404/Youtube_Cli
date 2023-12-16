
import pymysql

# Establish a connection to the MySQL database
connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='Sumit@123',
    database='youtube2',
    autocommit=True,
    # multipleStatements= True
)


def Delete_Videos(video_id):
    # Connect to the MySQL database

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure
        cursor.callproc('Delete_Videos', [video_id])

        # Commit the changes
        connection.commit()

        # print(f"Video with ID {video_id} deleted successfully.")
        
    except Exception as e:
        print(f"Error: {e}")


# Delete_Videos(1)

def Delete_Account(user_id):
    # Connect to the MySQL database

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure
        cursor.callproc('Delete_Account', [user_id])

        # Commit the changes
        connection.commit()

        # print(f"User with ID {user_id} account deleted successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
    


# Delete_Account(456)

    


def check_update_dislike_videos(user_id, videos_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure to check dislike videos
        cursor.callproc('CheckDislikeVideos', [user_id, videos_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        if len(results) == 0:
            # If there are no records, perform the update
            cursor.callproc('check_update_dislike_videos', [user_id, videos_id])

            # Commit the changes
            connection.commit()

            # print(f"Video not found in history. Updated dislike videos successfully.")
            
        else:
            # If there are results, you can handle them as needed
            # print("No need to update, it's already there")
            pass
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to check and update dislike videos
# check_update_dislike_videos(123, 456)



def check_update_liked_videos(user_id, videos_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure to check liked videos
        cursor.callproc('CheckLikedVideos', [user_id, videos_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        if len(results) == 0:
            # If there are no records, perform the update
            cursor.callproc('check_update_liked_videos', [user_id, videos_id])

            # Commit the changes
            connection.commit()

            # print(f"Video not found in history. Updated liked videos successfully.")
            
        else:
            # If there are results, you can handle them as needed
            # print("No need to update, it's already there")
            pass
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# check_update_liked_videos(123, 456)


def check_update_views(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure to check views
        cursor.callproc('CheckViews', [data["user_id"], data["id"]])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        if len(results) == 0:
            # If there are no records, perform the update
            cursor.callproc('check_update_views', [data["user_id"], data["id"]])

            # Commit the changes
            connection.commit()

            # print(f"Video not found in history. Updated views successfully.")
            
        else:
            # If there are results, you can handle them as needed
            # print("No need to update, it's already there")
            pass
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to check and update views
# check_update_views(123, 456)





def check_update_history(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure to check history
        cursor.callproc('check_update_hist', [data["user_id"], data["video_id"]])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        if len(results) == 0:
            # If there are no records, perform the update
            cursor.callproc('check_update_history', [data["user_id"], data["video_id"]])

            # Commit the changes
            connection.commit()

            # print(f"Video not found in history. Updated history successfully.")
            
        else:
            # If there are results, you can handle them as needed
            # print("No need to update, it's already there").
            pass
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to check and update history
# check_update_history(123, 456)










def payment_analytics(user_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for payment analytics
        cursor.callproc('payment_analytics', [user_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        analytics_data = []
        for result in results:
            analytics_data.append({
                'id': result[0],
                'Title': result[1],
                'views_count': result[2]
            })

        # Print or return the analytics data as needed
        return analytics_data
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to get payment analytics
# payment_analytics(123)






def your_subscribers(user_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for fetching subscribers
        cursor.callproc('your_subscribers', [user_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        subscribers_data = []
        for result in results:
            subscribers_data.append({
                'id': result[0],
                'Name': result[1]
            })

        # Print or return the subscribers data as needed
        return subscribers_data
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to get subscribers
# your_subscribers(123)







def your_subscriptions(user_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for fetching subscriptions
        cursor.callproc('your_subscriptions', [user_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        subscriptions_data = []
        for result in results:
            subscriptions_data.append({
                'id': result[0],
                'Name': result[1]
            })

        # Print or return the subscriptions data as needed
        return subscriptions_data
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to get subscriptions
# your_subscriptions(123)





def your_liked_videos(user_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for fetching liked videos
        cursor.callproc('your_liked_videos', [user_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        liked_videos_data = []
        for result in results:
            liked_videos_data.append({
                'id': result[0],
                'Title': result[1],
                'Description': result[2],
                'user_id': result[3]
                # Add other fields as needed
            })

        # Print or return the liked videos data as needed
        return liked_videos_data
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to get liked videos
# your_liked_videos(123)





def your_history_videos(user_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for fetching history videos
        cursor.callproc('your_history_videos', [user_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        history_videos_data = []
        for result in results:
            history_videos_data.append({
                'id': result[0],
                'Title': result[1],
                'Description': result[2],
                'user_id': result[3]
                # Add other fields as needed
            })

        # Print or return the history videos data as needed
        return history_videos_data
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to get history videos
# your_history_videos(123)





def your_videos(user_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for fetching user videos
        cursor.callproc('your_videos', [user_id])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        # print(results)
        user_videos_data = []
        for result in results:
            user_videos_data.append({
                'id': result[0],
                'Title': result[1],
                'Description': result[2],
                'user_id': result[3]
                # Add other fields as needed
            })

        # Print or return the user videos data as needed
        # print(user_videos_data
        return user_videos_data
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to get user videos
# your_videos(123)





def comments(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for fetching comments
        cursor.callproc('comments', [data["video_id"]])

        # Get the results
        results = cursor.fetchall()

        # Assuming 'results' is an array of rows
        comments_data = []
        for result in results:
            comments_data.append({
                'Text': result[0],
                'Name': result[1]
                # Add other fields as needed
            })

        # Print or return the comments data as needed
        # print(comments_data)
        return comments_data
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to get comments for a video
# comments(456)






def subscribing_channel(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for subscribing to a channel
        cursor.callproc('subscribing_channel', [data["user_id"], data["id"]])

        # Commit the changes
        connection.commit()

        # Print or return a success message
        # print("Subscribed successfully")
        
    except Exception as e:
        # Rollback the transaction in case of an error
        connection.rollback()
        print(f"Error: {e}")
    
    

# Example: Call the function to subscribe to a channel
# subscribing_channel(789, 123)





def check_subscription(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for checking subscriptions
        cursor.callproc('check_subscription', [data["user_id"], data["id"]])

        # Get the results
        results = cursor.fetchall()

        # Print or return the results as needed
        # print(results)
        return results
        
    except Exception as e:
        print(f"Error: {e}")
    
    

# Example: Call the function to check subscriptions
# check_subscription(789, 123)




def comment(text, user_id, video_id):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for adding comments
        cursor.callproc('comment', [text, user_id, video_id])

        # Commit the changes
        connection.commit()

        # Print or return a success message
        # print("Commented successfully")
        
    except Exception as e:
        # Rollback the transaction in case of an error
        connection.rollback()
        print(f"Error: {e}")
    
    

# Example: Call the function to add a comment
# comment("This is a great video!", 789, 123)




def subscriber(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for counting subscribers
        cursor.callproc('subscriber', [data["video_id"]])

        # Fetch the result
        result = cursor.fetchone()

        # Print or return the count of subscribers
        if result:
            count = result[0]
            # print(f"Number of Subscribers: {count}")
            return count
        else:
            # print("No subscribers found.")
            return 0
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
    
    

# Example: Call the function to count subscribers for a video
# video_subscriber_count = subscriber(123)




def dislike_videos(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for counting dislikes
        cursor.callproc('dislike_videos', [data["video_id"]])

        # Fetch the result
        result = cursor.fetchone()

        # Print or return the count of dislikes
        if result:
            count = result[0]
            # print(f"Number of Dislikes: {count}")
            return count
        else:
            # print("No dislikes found.")
            return 0
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
    
    

# Example: Call the function to count dislikes for a video
# video_dislike_count = dislike_videos(123)




def liked_videos(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for counting likes
        cursor.callproc('liked_videos', [data["video_id"]])

        # Fetch the result
        result = cursor.fetchone()

        # Print or return the count of likes
        if result:
            count = result[0]
            # print(f"Number of Likes: {count}")
            return count
        else:
            # print("No likes found.")
            return 0
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
    
    

# Example: Call the function to count likes for a video
# video_like_count = liked_videos(123)





def views(data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for counting views
        cursor.callproc('views', [data["video_id"]])

        # Fetch the result
        result = cursor.fetchone()

        # Print or return the count of views
        if result:
            count = result[0]
            # print(f"Number of Views: {count}")
            return count
        else:
            # print("No views found.")
            return 0
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
    
    

# Example: Call the function to count views for a video
# video_view_count = views(123)




def allusers():
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for retrieving all users
        cursor.callproc('allusers')

        # Fetch all the results
        results = cursor.fetchall()

        # Print or return the results
        user_videos_data = []
        for result in results:
            user_videos_data.append({
                'id': result[0],
                'Name': result[1],
                'Age': result[2],
                'Gender': result[3]
                # Add other fields as needed
            })
        return user_videos_data
        
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
    
    

# Example: Call the function to get all users
# all_users = users()





def videos_to_watch():
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for retrieving all videos
        cursor.callproc('videos_to_watch')

        # Fetch all the results
        results = cursor.fetchall()

        # Print or return the results
        # if results:
        #     for video in results:
        #         print(video)  # Adjust printing or processing as needed
        #     return results
        # else:
        #     print("No videos found.")
        #     return []
        user_videos_data = []
        for result in results:
            user_videos_data.append({
                'id': result[0],
                'Title': result[1],
                'Description': result[2],
                'user_id': result[3]
                # Add other fields as needed
            })
        return user_videos_data
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
    
    

# Example: Call the function to get all videos
# all_videos = videos_to_watch()





def video_upload(post_data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for video upload
        cursor.callproc('video_upload', (post_data['Title'], post_data['Description'], post_data['user_id']))

        # Commit the changes
        connection.commit()

        # Get the last inserted ID (assuming it's the video ID)
        # video_id = cursor.lastrowid
         
        cursor.execute("SELECT LAST_INSERT_ID() AS videos_id")
        result = cursor.fetchone()

        # Send a response
        if result:
            videos_id = result[0]
            # print('Signup successful. User ID:', user_id)
            return {'message': 'Signup Successfully', 'vidoes_id': videos_id} 
        else:
            raise Exception("Failed to fetch user ID")
        
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return {'error': 'Internal Server Error'}
    
    

# Example: Call the function to upload a video
post_data = {'Title': 'Sample Video', 'Description': 'This is a sample video.', 'user_id': 1}
# upload_response = video_upload(post_data)
# print(upload_response)





def login(post_data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for login
        cursor.callproc('login', (post_data['Email_ID'], post_data['Password'], post_data['user_id']))

        # Commit the changes
        connection.commit()

        # Get the last inserted ID (assuming it's the user ID)
        user_id = cursor.lastrowid

        # Send a response
        # print('Login request received successfully. User ID:', user_id)
        return {'message': 'Login Request Received Successfully'}
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return {'error': 'Internal Server Error'}
    
    

# Example: Call the function for login
# post_data = {'Email_ID': 'user@example.com', 'Password': 'password123', 'user_id': 3}
# login_response = login(post_data)
# print(login_response)





def users(post_data):
 
    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for user signup
        cursor.callproc('users', (post_data['Name'], post_data['Gender'], post_data['Age']))

        # Commit the changes to get the last inserted ID
        connection.commit()

        # Get the results from the stored procedure
        cursor.execute("SELECT LAST_INSERT_ID() AS user_id")
        result = cursor.fetchone()

        # Send a response
        if result:
            user_id = result[0]
            # print('Signup successful. User ID:', user_id)
            return {'message': 'Signup Successfully', 'user_id': user_id}
        else:
            raise Exception("Failed to fetch user ID")

    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return {'error': 'Internal Server Error'}
    
    

# Example: Call the function for user signup
# post_data = {'Name': 'John Doe', 'Gender': 'Male', 'Age': 25}
# signup_response = users(post_data)
# print(signup_response)






def login1(post_data):
    # Connect to the MySQL database
   

    try:
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Call the stored procedure for user login
        cursor.callproc('login1', (post_data['Email_ID'], post_data['Password']))

        # Get the results from the stored procedure
        # for result in cursor.stored_results():
        #     results = result.fetchall()
        results = cursor.fetchall()
        # Send a response
        # print('Login request received successfully. Results:', results)
        return {'message': 'Login Request Received Successfully', 'results': results}
        
    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return {'error': 'Internal Server Error'}
    
    

# Example: Call the function for user login






# finally:
#     # Close the cursor and connection
#     cursor.close()
#     connection.close()





import requests

flag=0
def Watch_Videos(response,user_id):

        # response1=requests.get("http://localhost:5000/users")
        # response1 =response1.json()["results"]
    response1=allusers()
    # print(response1)
        
     
    for video in response:
        print("ID : " + str(video["id"]))
        print("Title : "+video["Title"])
 
    while(1):

        print("\nEnter 1 to Watch Any Video.")
        print("Enter 0 to Go Back\n")
        p = int(input("Enter Integer : "))
        if(p==0):
            return 0
        else:
            video_id = int(input("\nEnter the ID of Video, You want to Watch : "));    
            print("")
        
            data={
                "user_id":user_id,
                "video_id":video_id
            } 

            # requests.post("http://localhost:5000/check_update_history",json=data) 
            check_update_history(data)
            
            
            for e in response:
                global flag
                if(e["id"]==video_id) :
                    flag=1
                    print("Title : "+e["Title"])
                    print("Description  : "+e["Description"])
                    # response=requests.post("http://localhost:5000/views",json=data)
                    # response=response.json()["results"]
                    response=views(data)
                    print("Views : " + str(response))
                    # response=requests.post("http://localhost:5000/liked_videos",json=data)
                    # response=response.json()["results"]
                    response=liked_videos(data)

                    print("Likes : " + str(response))
                    # response=requests.post("http://localhost:5000/dislike_videos",json=data)
                    # response=response.json()["results"]
                    response=dislike_videos(data)
                    print("Dislikes : " + str(response))

                    # response=requests.post("http://localhost:5000/subscriber",json=data)
                    # response=response.json()["results"]
                    response=subscriber(data)
                    print("Subscriber : " + str(response))

                    for j in response1 :
                            if(j["id"]==e["user_id"]):
                                print("Uploaded By "+j["Name"]) 

            if(flag==1):
                flag=0
                break
            else :
                print("Invalid ID, Plese Enter Correct ID.")  

                      
            
    data={
        "video_id":video_id
    } 
    # response=requests.post("http://localhost:5000/comments",json=data) 
    # response=response.json()["results"]
    response=comments(data)
    
    if(len(response)==0):
        print("\nNO Comments\n")
    else:
        print("\nComments\n")    
    for com in response:
        print("Comment : "+com["Text"])
        print("Commented By "+com["Name"]+"\n")

    
    
    

    data={
        "id":video_id,
        "user_id":user_id,
      
    }
    # requests.post("http://localhost:5000/check_update_views",json=data) 
    check_update_views(data)
    # response=requests.post("http://localhost:5000/check_subscription",json=data)
    # response=response.json()["results"]
    response=check_subscription(data)
    if(len(response)==0):
        print("You Haven't SubScribe this Channel")
        while(1):
            print("\nEnter 1 to Subscribe this Channel")
            print("Enter 2 to Do Nothing")
            print("Enter 0 to Go Back")
            
            k = int(input("\nEnter a Integer : "))
            if k==1:
                data = {
                "id":video_id,
                "user_id":user_id,
            
                
                } 
                # response=requests.post("http://localhost:5000/subscribing_channel",json=data)
                subscribing_channel(data)
                break
            elif k==0:
                return 
            elif k==2:
                break
            else:
                print("Invalid Input, Type Again.")
        
                






    else:
        print("You Have Already SubScribed this Channel")

   
    while(1):   
        print("\nEnter 1 to like ")
        print ("Enter 2 to Dislike ")
        print("Enter 3 to Do Nothing.") 
        print("Enter 0 to Go Back")   

        k= int(input("\nEnter a integer : ")) 
        

        data={
            "user_id":user_id,
            "videos_id":video_id
        }
        if k==1:
            # requests.post("http://localhost:5000/check_update_liked_videos",json=data)
            check_update_liked_videos(user_id,video_id)
            break
        elif k==2:  
            # requests.post("http://localhost:5000/check_update_dislike_videos",json=data) 
            check_update_dislike_videos(user_id,video_id)  
            break 
        elif k==3:
            break
        elif k==0:
            return    



    


    while(1):
        print("\nEnter 1 to Comment")
        print("Enter 2 to Do Nothing")
        print("Enter 0 to Go Back")
        
        k = int(input("\nEnter a Integer : "))
        if k==1:
                text=input("Enter Text to Comment : ")
                video_data = {
                "id":video_id,
                "user_id":user_id,
                "text":text
                
                } 
                # response=requests.post("http://localhost:5000/comment",json=video_data)
                comment(text,user_id,video_id)
                break
        elif k==2:
            break
        elif k==0:
            return


   

def app(user_id):

    while(1):
        print("\nPress 1 to Watch Videos")  
        print("Press 2 to Upload Videos")
        print("Press 3 to Watch Your Videos")
        print("Press 4 to Watch History")
        print("Press 5 to Watch Liked Videos")
        print("Press 6 to Watch Subscriptions")
        print("Press 7 to Watch Analytics")
        print("Press 8 to Manage Your Videos")
        print("Press 9 to Delete Account")
        print("Press 10 to Log Out")
    
        a = int(input("\nEnter Here : "))
        

        if a==1:
            # response=requests.get("http://localhost:5000/videos_to_watch")
            response=videos_to_watch()
            
            # response1 =response["results"]
            # print(response1)
            # print(response)
            
            print("\nVideos \n")
            if(len(response)==0):
                print("No Videos to Watch, Please Upload.")
            else:    
                k=Watch_Videos(response,user_id)
                if(k==0) :
                    continue
                else :
                    print("\nYou have Succesfully Watched video\n")

        elif a==2:
            Title = input("\nEnter Title : ") 
            Description = input("Enter Description : ")
            zero=0
            data={
            "Title" : Title,
            "Description" : Description,
            "user_id" : user_id

            }
            # response = requests.post("http://localhost:5000/video_upload",json=data)  
            video_id=video_upload(data)
            print("\nVideo  Successfully Uploaded.")

        elif a==3:
            
            data={
                "user_id":user_id
            }
            # response=requests.post("http://localhost:5000/your_videos",json=data)
            # response=response.json()["results"]
            response=your_videos(user_id)
            # print(response)
            print("\nYour Videos \n")

            if(len(response)==0):
                print("No Videos, Please Upload.")
            else:    
                k=Watch_Videos(response,user_id)
                if(k==0) :
                    continue
                else :
                    print("\nYou have Succesfully Watched video\n")
           



        elif a==4:
            data={
                "user_id":user_id
            }
            # response=requests.post("http://localhost:5000/your_history_videos",json=data)
            # response=response.json()["results"]
            response=your_history_videos(user_id)
            print("\nYour History Videos \n")
            
            if(len(response)==0):
                print("No Videos, Please Watch Videos.")
            else:    
                k=Watch_Videos(response,user_id)
                if(k==0) :
                    continue
                else :
                    print("\nYou have Succesfully Watched video\n")
     

        elif a==5:
             
            data={
                "user_id":user_id
            }
            # response=requests.post("http://localhost:5000/your_liked_videos",json=data)
            # response=response.json()["results"]
            response=your_liked_videos(user_id)
            print("\nYour Liked Videos \n")

            if(len(response)==0):
                print("No Videos, Please Like Videos.")
            else:    
                k=Watch_Videos(response,user_id)
                if(k==0) :
                    continue
                else :
                    print("\nYou have Succesfully Watched video\n")

        elif a==6:

            data={
                "user_id":user_id
            }    


            # response=requests.post("http://localhost:5000/your_subscriptions",json=data)
            # response=response.json()["results"]
            response=your_subscriptions(user_id)
            print("\nYour Subscriptions\n")

            if(len(response)==0):
                print("No Subscriptions, Please Subscribe Channel.")
            else:    
                for e in response:
                    print("ID : "+str(e["id"]))
                    print("Name : "+str(e["Name"]) )
        

        elif a==7:
            while(1):
                print("\nPress 1 to Watch Your Subscribers")
                print("Press 2 to Watch Your Payment Analytics")
                print("Press 0 to Go Back \n")
                
                k=int(input("Enter a integer : "))
                if k==1:
                    data={
                    "user_id":user_id
                    }    


                    # response=requests.post("http://localhost:5000/your_subscribers",json=data)
                    # response=response.json()["results"]
                    response=your_subscribers(user_id)
                    print("\nYour Subscribers\n")

                    if(len(response)==0):
                        print("No Subscribers.")
                    else:    
                        for e in response:
                            print("ID : "+str(e["id"]))
                            print("Name : "+str(e["Name"]) )

                    
        

                elif k==2:
                    data={
                    "user_id":user_id
                    }  
                    
                    # response=requests.post("http://localhost:5000/payment_analytics",json=data)
                    # response=response.json()["results"]
                    response=payment_analytics(user_id)
                    print("\nPayment Analytics\n")
                    
                    sum=0
                    for e in response:
                        print("Title : "+str(e["Title"]) )
                        print("Views : "+str(e["views_count"])+"\n" )
                        sum=sum+e["views_count"]
        
                    
                    print("Total Views : "+str(sum))
                    print("Total Revenue : Rs "+str(sum/2))

                elif k==0:
                    break;  

                else:
                    print("Invalid Input, Type Again.")  

        elif a==8:
            data={
                "user_id":user_id
            }
            # response=requests.post("http://localhost:5000/your_videos",json=data)
            # response=response.json()["results"]
            response=your_videos(user_id)
            print("\nYour Videos\n")

            if(len(response)==0):
                print("No Videos, Please Upload.")
            else:    
                for video in response:
                    print("ID : " + str(video["id"]))
                    print("Title : "+video["Title"]+"\n")

                video_id=input("Enter the ID of Video, You want to delete : ")  
                data={
                    "video_id":video_id
                } 
                # response=requests.post("http://localhost:5000/Delete_Videos",json=data)

                Delete_Videos(video_id)
                
                print("\nVideo Successfully Deleted.")
        elif a==9:
            while(1):
                data={
                    "user_id":user_id
                    }  
                    
                s=input("\nDo You Really Want to Delete Your Account(Yes/No) : ")
                if(s=="Yes"):
                    # response=requests.post("http://localhost:5000/Delete_Account",json=data)
                    # response=response.json()["results"]
                    Delete_Account(user_id)
                    print("\nAccount Successfully Deleted.")
                    return 1
                elif s=="No" :
                    break
                else:
                    print("Invalid Input Type Again.")
        elif a==10:
            print("\nThankYou For Visiting Us.")
            return 1        
        else:
            print("Invalid Input, Type Again.")  





           








print("\n!!! WELCOME TO THE YOUTUBE !!!\n")

while(1):
    
    print("\nPress 1 to LOGIN")
    print("Press 2 to SIGNUP")
    print("Press 3 to EXIT") 
    a = int(input("\nEnter Here : "))
    if a==1:
        email_id = input("\nEnter your Email ID : ")
        password = input("Enter your Password : ")
        data1 = {
        'Email_ID': email_id,
        'Password': password,
        }
      
        response = login1(data1)
        # print(response["results"][0][0])
        if len(response["results"]) != 0:
            print("\nYou have login succesfully")
            response=response["results"][0][0]
            p=app(response)
            if(p==1):
                continue
            else:
                break
            
        else :
            print("\nInvalid Password or Email_id")  

    elif a==2:
        Name = input("\nEnter your Name : ")
        Age = input("Enter your Age : ") 
        Gender = input("Enter your Gender(M/F) : ")
        email_id = input("Enter your Email ID : ")
        password = input("Enter your Password : ")


        
        data = {
        'Name': Name,
        'Age': Age,
        'Gender': Gender
        }

      
       
        data2 = {
        'Email_ID': email_id,
        'Password': password
        }
    

        response = login1(data2)
    

        if len(response["results"]) != 0:
            print("\nUser Already exists, Please Login")
            continue
            
        
        
        signup_response = users(data)
        
        data1 = {
        'Email_ID': email_id,
        'Password': password,
        'user_id': signup_response["user_id"]
        }

       

        login_response = login(data1)
        
        print("\nAccount Created successfully.")
        continue

        
            
    elif a==3:
        print("\nThankyou for Visiting Us.\n")
        break

    else:
        print("Invalid Input. Type Again.")





    