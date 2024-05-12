from fastapi import APIRouter
from models.posts import Post
from models.posts import Comment
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router=APIRouter()

@router.get("/")
async def get_posts():
    try:
        posts=list_serial(collection_name.find())
        return posts
    except Exception as e:
        return{"message":f"Error retreving post:{str(e)}"}
    
@router.get("/{id}")
async def get_one_post(id:str):
    try:
        post=list_serial(collection_name.find(id))
        return post
    except Exception as e:
        return{"message":f"Error retreving post:{str(e)}"}



@router.post("/")
async def create_post(post: Post):
    try:
        collection_name.insert_one(dict(post))
        return {"message":"Blog Post created successfully"}
    except Exception as e:
         return {"message": f"Error creating post: {str(e)}"}


@router.put("/{id}")
async def update_post(id:str, post:Post):
    try:
        result=collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(post)})
        
        if result is None:
            return {"message": "Post not found"}
        return{"message": "Post updated successfully!"}
      
    except Exception as e:
         return {"message": f"Error updating post: {str(e)}"}


@router.delete("/{id}")
async def delete_post(id:str):
    try:
        result=collection_name.find_one_and_delete({"_id":ObjectId(id)})
        if result is None:
            return {"message": "Post not found"}
        return{"message": "Post deleted successfully!"}
      
    except Exception as e:
         return {"message": f"Error updating post: {str(e)}"}



@router.patch("/{id}/comments")
async def put_comment(id: str, comment:Comment ): 
   
  try:
    update_result = collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$push": {"comments": dict(comment)}}  
    )
    
    if update_result is None:
         return {"message": "Post not found"}
    
    return {"message": "Comment added successfully!"}
  
  except Exception as e:
        return {"message": f"Error updating post: {str(e)}"}

  
@router.delete("/{id}/comments/{com_id}")
async def delete_comment(id: str, com_id: str): 
   
  try:
    update_result = collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$pull": {"comments": {"id": com_id}}}  
    )
    
    if update_result is None:
        return {"message": "Post not found"}
    
    return {"message": "Comment deleted successfully!"}
  
  except Exception as e:
         return {"message": f"Error updating post: {str(e)}"}
  

@router.patch("/{id}/like")
async def update_like(id:str):
    try:
    
        update_result = collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$inc": {"likes": 1}} 
    )
        
        if update_result is None:
            return {"message": "Post not found"}

        return {"message": "Like updated successfully!"}
    
    except Exception as e:
         return {"message": f"Error updating post: {str(e)}"}

@router.patch("/{id}/dislike")
async def update_dislike(id:str):
    try:

        update_result = collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$inc": {"dislikes": 1}} 
    )
        
        if update_result is None:
            return {"message": "Post not found"}

        return {"message": "Dislike updated successfully!"}
    
    except Exception as e:
         return {"message": f"Error updating post: {str(e)}"}


