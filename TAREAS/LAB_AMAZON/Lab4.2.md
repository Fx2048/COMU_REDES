# LABORATORY FROM 4.1 AMAZON WEB SERVICES: CREATE A BUCKET
Description Notes about the Session:
# Task 1:

![OBJECT INDEX](https://github.com/Fx2048/COMU_REDES/assets/131219987/3ab04894-dcee-4977-8582-19eac3976265)

![OSO CREATION GNEERAL BUCKET](https://github.com/Fx2048/COMU_REDES/assets/131219987/6c5a387a-265f-4376-a7b4-df3b16aba374)

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

![OUTPUT FOLLOW LEADER](https://github.com/Fx2048/COMU_REDES/assets/131219987/1a6a4b0c-bca0-4054-bbae-75f234d19631)
