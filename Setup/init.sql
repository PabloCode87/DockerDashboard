--
-- PostgreSQL database dump
--

-- Dumped from database version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Alert; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Alert" (
    id integer NOT NULL,
    "containerId" text NOT NULL,
    name text NOT NULL,
    condition text NOT NULL,
    threshold double precision NOT NULL,
    "createdAt" timestamp(3) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public."Alert" OWNER TO postgres;

--
-- Name: Alert_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Alert_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Alert_id_seq" OWNER TO postgres;

--
-- Name: Alert_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Alert_id_seq" OWNED BY public."Alert".id;


--
-- Name: DockerContainer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."DockerContainer" (
    id integer NOT NULL,
    "containerId" text NOT NULL,
    name text NOT NULL,
    status text NOT NULL,
    image text NOT NULL,
    "createdAt" timestamp(3) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    "cpuUsage" double precision,
    "memoryUsage" double precision
);


ALTER TABLE public."DockerContainer" OWNER TO postgres;

--
-- Name: DockerContainer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."DockerContainer_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."DockerContainer_id_seq" OWNER TO postgres;

--
-- Name: DockerContainer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."DockerContainer_id_seq" OWNED BY public."DockerContainer".id;


--
-- Name: LogEntry; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."LogEntry" (
    id integer NOT NULL,
    "containerId" text NOT NULL,
    message text NOT NULL,
    level text NOT NULL,
    "timestamp" timestamp(3) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public."LogEntry" OWNER TO postgres;

--
-- Name: LogEntry_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."LogEntry_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."LogEntry_id_seq" OWNER TO postgres;

--
-- Name: LogEntry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."LogEntry_id_seq" OWNED BY public."LogEntry".id;


--
-- Name: _prisma_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public._prisma_migrations (
    id character varying(36) NOT NULL,
    checksum character varying(64) NOT NULL,
    finished_at timestamp with time zone,
    migration_name character varying(255) NOT NULL,
    logs text,
    rolled_back_at timestamp with time zone,
    started_at timestamp with time zone DEFAULT now() NOT NULL,
    applied_steps_count integer DEFAULT 0 NOT NULL
);


ALTER TABLE public._prisma_migrations OWNER TO postgres;

--
-- Name: Alert id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Alert" ALTER COLUMN id SET DEFAULT nextval('public."Alert_id_seq"'::regclass);


--
-- Name: DockerContainer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."DockerContainer" ALTER COLUMN id SET DEFAULT nextval('public."DockerContainer_id_seq"'::regclass);


--
-- Name: LogEntry id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."LogEntry" ALTER COLUMN id SET DEFAULT nextval('public."LogEntry_id_seq"'::regclass);


--
-- Data for Name: Alert; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Alert" (id, "containerId", name, condition, threshold, "createdAt") FROM stdin;
1	abc123	Alerta de CPU alta	CPU >	80.5	2025-08-21 11:44:10.458
\.


--
-- Data for Name: DockerContainer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."DockerContainer" (id, "containerId", name, status, image, "createdAt", "cpuUsage", "memoryUsage") FROM stdin;
1	abc123	python3.14	running	python:3.14	2025-08-10 20:10:33.914	2.5	128
2	def456	python-latest	exited	python:latest	2025-08-10 20:10:33.914	0	0
3	ghi789	python3.12	paused	python:3.12	2025-08-10 20:10:33.914	1.2	64
\.


--
-- Data for Name: LogEntry; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."LogEntry" (id, "containerId", message, level, "timestamp") FROM stdin;
1	abc123	Iniciando contenedor abc123...	INFO	2025-08-11 12:06:24.106
2	abc123	Instalando dependencias...	INFO	2025-08-11 12:11:24.106
3	abc123	Contenedor abc123 en ejecución sin errores.	INFO	2025-08-11 12:16:24.106
4	def456	Contenedor def456 detenido.	WARN	2025-08-11 12:01:24.146
5	def456	Reinicio programado pendiente.	INFO	2025-08-11 12:15:24.146
6	ghi789	Contenedor ghi789 en pausa por mantenimiento.	INFO	2025-08-11 11:46:24.148
\.


--
-- Data for Name: _prisma_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public._prisma_migrations (id, checksum, finished_at, migration_name, logs, rolled_back_at, started_at, applied_steps_count) FROM stdin;
78e69419-0e67-4ebd-a466-24b28b34bd8e	72f01a5c0ed722e754bcc8646b43c5681206fc638c1dacd4f5ad528eaa141221	2025-08-05 13:10:25.911606+02	20250805111025_init	\N	\N	2025-08-05 13:10:25.884852+02	1
2bd1eaa9-4141-4630-88f0-81cd72f72e6c	e3bd94578c0c09107dd2fbc8644388bf4f1d4ead08357bdc670f7eefb2973d35	2025-08-06 14:07:35.598332+02	20250806120735_add_cpu_memory_usage	\N	\N	2025-08-06 14:07:35.593523+02	1
\.


--
-- Name: Alert_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Alert_id_seq"', 1, true);


--
-- Name: DockerContainer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."DockerContainer_id_seq"', 4, true);


--
-- Name: LogEntry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."LogEntry_id_seq"', 6, true);


--
-- Name: Alert Alert_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Alert"
    ADD CONSTRAINT "Alert_pkey" PRIMARY KEY (id);


--
-- Name: DockerContainer DockerContainer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."DockerContainer"
    ADD CONSTRAINT "DockerContainer_pkey" PRIMARY KEY (id);


--
-- Name: LogEntry LogEntry_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."LogEntry"
    ADD CONSTRAINT "LogEntry_pkey" PRIMARY KEY (id);


--
-- Name: _prisma_migrations _prisma_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public._prisma_migrations
    ADD CONSTRAINT _prisma_migrations_pkey PRIMARY KEY (id);


--
-- Name: DockerContainer_containerId_key; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "DockerContainer_containerId_key" ON public."DockerContainer" USING btree ("containerId");


--
-- Name: Alert Alert_containerId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Alert"
    ADD CONSTRAINT "Alert_containerId_fkey" FOREIGN KEY ("containerId") REFERENCES public."DockerContainer"("containerId") ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: LogEntry LogEntry_containerId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."LogEntry"
    ADD CONSTRAINT "LogEntry_containerId_fkey" FOREIGN KEY ("containerId") REFERENCES public."DockerContainer"("containerId") ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- PostgreSQL database dump complete
--

