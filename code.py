#!/usr/bin/python python2.7
import psycopg2


def printArticles(cursor):
    for (author, views) in cursor.fetchall():
        print("    \"{}\"- {} views".format(author, views))


def printAuthors(cursor):
    for (author, views) in cursor.fetchall():
        print("    {} - {} views".format(author, views))


def printErrorDays(cursor):
    for (date, errors) in cursor.fetchall():
        date = date.strftime("%B %d, %Y")
        print("    {} - {:.2f} errors".format(date, errors))


def main():
    connection = psycopg2.connect("dbname=news")
    cursor = connection.cursor()
    print("1. What are the most popular three articles of all time?")
    most_popular_articles = """
        SELECT article.title,
        COUNT(log_record.path) AS views
        FROM log AS log_record,
        articles AS article
        WHERE '/article/' ||article.slug = log_record.path
        GROUP BY article.title
        ORDER BY views DESC
        LIMIT 3;
    """
    cursor.execute(most_popular_articles)
    printArticles(cursor)

    print("2. Who are the most popular article authors of all time?")

    most_popular_article_authors = """
        SELECT author.name,
        COUNT(log_record.path) AS views
        FROM authors AS author,
        log AS log_record,
        articles AS article
        WHERE author.id = article.author
        AND '/article/' ||article.slug = log_record.path
        GROUP BY author.name
        ORDER BY views DESC
    """
    cursor.execute(most_popular_article_authors)

    printAuthors(cursor)

    print("3. On which days did more than 1% of requests lead to errors?")

    days_with_most_errors = """
    DROP VIEW IF EXISTS status_count;
    CREATE VIEW status_count AS
    SELECT log_record.time::date AS date,
    SUM(CASE WHEN log_record.status NOT LIKE '200 OK' THEN 1 ELSE 0 END)
    AS  error_status,
    COUNT(*) AS total_status
    FROM log AS log_record
    GROUP BY date;
    SELECT date,
    CAST(error_status AS FLOAT)*100/total_status AS error_ratio
    FROM status_count
    WHERE (CAST( error_status AS FLOAT)*100/total_status)>1
    GROUP BY date, error_status, total_status
    ORDER BY  error_ratio DESC;
    """
    cursor.execute(days_with_most_errors)
    printErrorDays(cursor)


if __name__ == "__main__":
    main()
