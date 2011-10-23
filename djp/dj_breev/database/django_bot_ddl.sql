CREATE TABLE "djangobot_task" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(255) NOT NULL UNIQUE,
    "script" text NOT NULL,
    "interval_days" integer CHECK ("interval_days" >= 0) NOT NULL,
    "interval_hours" integer CHECK ("interval_hours" >= 0) NOT NULL,
    "interval_minutes" integer CHECK ("interval_minutes" >= 0) NOT NULL,
    "next_execution" timestamp with time zone NOT NULL,
    "last_execution" timestamp with time zone NOT NULL,
    "status" varchar(50) NOT NULL,
    "last_result" varchar(255) NOT NULL,
    "enabled" boolean NOT NULL
)
;

