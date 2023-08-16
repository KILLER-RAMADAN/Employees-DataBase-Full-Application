import sqlite3

class databsae():
    
    def __init__(self,db):
        
        self.sq_con=sqlite3.connect(db)
        self.cur=self.sq_con.cursor()
        
        self.quary="""
        
        CREATE TABLE IF NOT EXISTS Employee (
            
            Id Integer Primary key,
            Name text,
            Jop text,
            Gender text,
            Age text,
            Email text,
            Phone text,
            Address text,
            Image BloP
        )
    
        """
        
        self.cur.execute(self.quary)
        
        self.sq_con.commit()
        
    def insert_date(self,Id,Name,Jop,Gender,Age,Email,Phone,Address,Image):
        
     
        self.cur.execute("INSERT INTO Employee values (?,?,?,?,?,?,?,?,?)",(Id,Name,Jop,Gender,Age,Email,Phone,Address,Image))
        
        self.sq_con.commit()
    
    
    def fetche_all(self):
        self.quary2="""SELECT * FROM Employee"""
        self.rows=self.cur.execute(self.quary2).fetchall()
        
        return self.rows
        
    def remove(self,Id):
        self.cur.execute(" DELETE FROM Employee WHERE Id=?",(Id,))
        self.sq_con.commit()
        
    def add_image(self,Id):
        self.rows=self.cur.execute(" Select * FROM Employee WHERE Id=?",(Id,))
        return self.rows
        
    
        
    def ubdate_data(self,Id,Name,Jop,Gender,Age,Email,Phone,Address,Image):
        
        self.cur.execute("Update Employee set Name=?,Jop=?,Gender=?,Age=?,Email=?,Phone=?,Address=?,Image=? WHERE Id=? ",(Name,Jop,Gender,Age,Email,Phone,Address,Image,Id))
        
        self.sq_con.commit()
     
     
     
    def serche_data(self,Ct,Et):
        self.cur.execute("SELECT * FROM Employee WHERE " +Ct+" like '%'||?||'%'", (Et,))
        self.rows=self.cur.fetchall()
        return self.rows
    
    
        
      