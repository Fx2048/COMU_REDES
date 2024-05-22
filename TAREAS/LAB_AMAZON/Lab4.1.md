Description Notes about the Session:


````
{
    "Version":"2012-10-17",
    "Statement":[
        {
            "Sid":"PublicReadGetObject",
            "Effect":"Allow",
            "Principal":"*",
            "Action":[
                "s3:GetObject"
            ],
            "Resource":[
                "arn:aws:s3:::example-bucket/*"
            ]
        }
    ]
} 

````

#for the policy version  and edit intructions

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1a6a4b0c-bca0-4054-bbae-75f234d19631)
